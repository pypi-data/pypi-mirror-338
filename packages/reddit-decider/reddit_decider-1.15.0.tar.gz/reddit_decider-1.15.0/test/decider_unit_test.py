#!/usr/bin/env python
import json
import os

from contextlib import contextmanager
from unittest import TestCase
from unittest.mock import ANY

from rust_decider import Decider
from rust_decider import DeciderException
from rust_decider import DeciderInitException
from rust_decider import FeatureNotFoundException
from rust_decider import ValueTypeMismatchException
from rust_decider import version
from utils import AD_ACCOUNT_ID
from utils import BUSINESS_ID
from utils import CANONICAL_URL
from utils import create_temp_config_file
from utils import ctx_dict
from utils import DEVICE_ID
from utils import event_json
from utils import GEN_EXP_ID
from utils import GEN_EXP_NAME
from utils import GEN_EXP_VERSION
from utils import SUBREDDIT_ID
from utils import USER_ID

TEST_DIR = os.path.dirname(os.path.abspath(__file__))


def setup_decider_class(cfg_path):
    return Decider(cfg_path)


@contextmanager
def test_feature_not_found():
    with create_temp_config_file({}) as f:
        decider = setup_decider_class(f.name)
        yield decider


class TestDecider(TestCase):
    def setUp(self):
        self.valid_ctx_dict = ctx_dict

        variants = [
            {"range_start": 0.0, "range_end": 0.2, "name": "control_1"},
            {"range_start": 0.2, "range_end": 0.4, "name": "variant_2"},
            {"range_start": 0.4, "range_end": 0.6, "name": "variant_3"},
            {"range_start": 0.6, "range_end": 0.8, "name": "variant_4"},
            {"range_start": 0.8, "range_end": 1.0, "name": "variant_5"},
        ]

        self.device_id_exp = self.config_for_bucket_val("device_id", variants)

        self.canonical_url_exp = self.config_for_bucket_val("canonical_url", variants)

        self.subreddit_id_exp = self.config_for_bucket_val("subreddit_id", variants)

        self.ad_account_id_exp = self.config_for_bucket_val("ad_account_id", variants)

        self.business_id_exp = self.config_for_bucket_val("business_id", variants)

        self.genexp_0_cfg = {
            "genexp_0": {
                "id": GEN_EXP_ID,
                "name": GEN_EXP_NAME,
                "enabled": True,
                "version": GEN_EXP_VERSION,
                "emit_event": True,
                "type": "range_variant",
                "start_ts": 0,
                "stop_ts": 2147483648,
                "experiment": {
                    "variants": variants,
                    "experiment_version": 5,
                    "shuffle_version": 91,
                    "bucket_val": "user_id",
                    "log_bucketing": False,
                },
            },
        }

        self.additional_2_exp = {
            "exp_0": {
                "id": 3248,
                "name": "exp_0",
                "enabled": True,
                "version": "5",
                "type": "range_variant",
                "emit_event": True,
                "start_ts": 37173982,
                "stop_ts": 2147483648,
                "experiment": {
                    "variants": [
                        {"range_start": 0.0, "range_end": 0.2, "name": "control_1"},
                        {"range_start": 0.2, "range_end": 0.4, "name": "control_2"},
                        {"range_start": 0.4, "range_end": 0.6, "name": "variant_2"},
                        {"range_start": 0.6, "range_end": 0.8, "name": "variant_3"},
                        {"range_start": 0.8, "range_end": 1.0, "name": "variant_4"},
                    ],
                    "experiment_version": 5,
                    "shuffle_version": 91,
                    "bucket_val": "user_id",
                    "log_bucketing": False,
                },
            },
            "exp_1": {
                "id": 3246,
                "name": "exp_1",
                "enabled": True,
                "version": "5",
                "type": "range_variant",
                "emit_event": True,
                "start_ts": 37173982,
                "stop_ts": 2147483648,
                "experiment": {
                    "variants": [
                        {"range_start": 0, "range_end": 0, "name": "variant_0"}
                    ],
                    "experiment_version": 5,
                    "shuffle_version": 0,
                    "bucket_val": "user_id",
                    "log_bucketing": False,
                },
            },
        }

        super().setUp()

    def config_for_bucket_val(self, bv, variants):
        genexp_config = {
            "id": 123,
            "name": "genexp_device_id",
            "enabled": True,
            "version": "5",
            "type": "range_variant",
            "start_ts": 0,
            "stop_ts": 2147483648,
            "emit_event": True,
            "experiment": {
                "variants": variants,
                "experiment_version": 5,
                "shuffle_version": 91,
                "bucket_val": None,
                "log_bucketing": False,
            },
        }

        exp_name = f"genexp_{bv}"

        config = {exp_name: {**genexp_config, **{"name": exp_name}}}

        config[exp_name]["experiment"]["bucket_val"] = bv

        return config

    def assert_event_json(
        self,
        ctx,
        event,
        noun,
        variant,
        experiment_name=GEN_EXP_NAME,
        experiment_id=GEN_EXP_ID,
        decision_kind="FracAvail",
        bucket_val=None,
        is_override=False,
    ):
        self.assertEqual(
            dict(event),
            {"decision_kind": decision_kind, "exposure_key": ANY, "json_str": ANY},
        )
        self.assertEqual(
            json.loads(event.json_str),
            event_json(
                ctx,
                noun,
                variant,
                experiment_name,
                experiment_id,
                is_override,
                bucket_val,
            ),
        )

    def test_init(self):
        # handles full cfg.json file
        decider = setup_decider_class(f"{TEST_DIR}/../../cfg.json")
        self.assertEqual(type(decider), Decider)

    def test_init_missing_cfg_file(self):
        with self.assertRaises(DeciderInitException) as e:
            setup_decider_class("foo")
        self.assertEqual(
            str(e.exception),
            "Decider initialization failed: Std io error: No such file or directory (os error 2)",
        )

    def test_init_bad_cfg(self):
        # an experiment's id is string instead of int
        cfg = {
            "exp_0": {
                "id": "3248",
                "name": "exp_0",
                "enabled": True,
                "version": "5",
                "type": "range_variant",
                "start_ts": 37173982,
                "stop_ts": 2147483648,
                "experiment": {
                    "variants": [],
                    "experiment_version": 5,
                    "shuffle_version": 91,
                    "bucket_val": "user_id",
                    "log_bucketing": False,
                },
            }
        }

        with create_temp_config_file(cfg) as f:
            with self.assertLogs() as captured:
                setup_decider_class(f.name)

            assert any(
                'Partially loaded Decider: 1 feature(s) failed to load: {"exp_0": ParsingError(Error("invalid type: string \\"3248\\", expected u32'
                in x.getMessage()
                for x in captured.records
            )

    def test_init_partially_bad_cfg(self):
        cfg = self.genexp_0_cfg
        invalid_exp = {"some_key": [1, 2, 3]}
        cfg.update(invalid_exp)

        with create_temp_config_file(cfg) as f:
            with self.assertLogs() as captured:
                decider = setup_decider_class(f.name)

                assert any(
                    'Partially loaded Decider: 1 feature(s) failed to load: {"some_key": ParsingError(Error("version field missing or unrecognized"'
                    in x.getMessage()
                    for x in captured.records
                )

                choice = decider.choose("genexp_0", self.valid_ctx_dict)

                self.assertEqual(
                    dict(choice),
                    {
                        "variant": "variant_5",
                        "value": None,
                        "feature_id": 6299,
                        "feature_name": "genexp_0",
                        "feature_version": 5,
                        "events": [
                            f"0::::6299::::genexp_0::::5::::variant_5::::{USER_ID}::::user_id::::0::::2147483648"
                        ],
                        "full_events": ANY,
                    },
                )

                assert len(choice.full_events) == 1
                self.assert_event_json(
                    self.valid_ctx_dict, choice.full_events[0], "user_id", "variant_5"
                )

    def test_choose(self):
        with create_temp_config_file(self.genexp_0_cfg) as f:
            decider = setup_decider_class(f.name)

            choice = decider.choose("genexp_0", self.valid_ctx_dict)

            self.assertEqual(
                dict(choice),
                {
                    "variant": "variant_5",
                    "value": None,
                    "feature_id": 6299,
                    "feature_name": "genexp_0",
                    "feature_version": 5,
                    "events": [
                        f"0::::6299::::genexp_0::::5::::variant_5::::{USER_ID}::::user_id::::0::::2147483648"
                    ],
                    "full_events": ANY,
                },
            )
            assert len(choice.full_events) == 1
            self.assert_event_json(
                self.valid_ctx_dict, choice.full_events[0], "user_id", "variant_5"
            )

    def test_choose_without_variant(self):
        cfg = self.genexp_0_cfg
        variants = [
            {"name": "enabled", "size": 0, "range_end": 0, "range_start": 0},
            {"name": "control_1", "size": 0, "range_end": 0, "range_start": 0},
        ]
        cfg["genexp_0"]["experiment"]["variants"] = variants

        with create_temp_config_file(cfg) as f:
            decider = setup_decider_class(f.name)

            choice = decider.choose("genexp_0", self.valid_ctx_dict)

            self.assertEqual(
                dict(choice),
                {
                    "variant": None,
                    "value": None,
                    "feature_id": 6299,
                    "feature_name": "genexp_0",
                    "feature_version": 5,
                    "events": [],
                    "full_events": [],
                },
            )

    def test_choose_without_ctx(self):
        with create_temp_config_file(self.genexp_0_cfg) as f:
            decider = setup_decider_class(f.name)

            with self.assertRaises(DeciderException) as e:
                decider.choose("genexp_0", None)

            self.assertEqual(
                str(e.exception),
                "Missing `context` param for feature_name: genexp_0",
            )

    def test_choose_bucket_val_device_id(self):
        with create_temp_config_file(self.device_id_exp) as f:
            decider = setup_decider_class(f.name)

            choice = decider.choose("genexp_device_id", self.valid_ctx_dict)

            self.assertEqual(
                dict(choice),
                {
                    "variant": "variant_4",
                    "value": None,
                    "feature_id": 123,
                    "feature_name": "genexp_device_id",
                    "feature_version": 5,
                    "events": [
                        f"0::::123::::genexp_device_id::::5::::variant_4::::{DEVICE_ID}::::device_id::::0::::2147483648"
                    ],
                    "full_events": ANY,
                },
            )
            assert len(choice.full_events) == 1
            self.assert_event_json(
                self.valid_ctx_dict,
                choice.full_events[0],
                "device_id",
                "variant_4",
                "genexp_device_id",
                123,
            )

    def test_choose_bucket_val_device_id_missing_identifier(self):
        with create_temp_config_file(self.device_id_exp) as f:
            decider = setup_decider_class(f.name)
            ctx = self.valid_ctx_dict.copy()
            del ctx["device_id"]

            with self.assertRaises(DeciderException) as e:
                decider.choose("genexp_device_id", ctx)

            self.assertEqual(
                str(e.exception),
                'Missing field "device_id" in context for bucket_val = device_id',
            )

    def test_choose_bucket_val_canonical_url(self):
        with create_temp_config_file(self.canonical_url_exp) as f:
            decider = setup_decider_class(f.name)

            choice = decider.choose("genexp_canonical_url", self.valid_ctx_dict)

            self.assertEqual(
                dict(choice),
                {
                    "variant": "variant_3",
                    "value": None,
                    "feature_id": 123,
                    "feature_name": "genexp_canonical_url",
                    "feature_version": 5,
                    "events": [
                        f"0::::123::::genexp_canonical_url::::5::::variant_3::::{CANONICAL_URL}::::canonical_url::::0::::2147483648"
                    ],
                    "full_events": ANY,
                },
            )
        assert len(choice.full_events) == 1
        self.assert_event_json(
            self.valid_ctx_dict,
            choice.full_events[0],
            "canonical_url",
            "variant_3",
            "genexp_canonical_url",
            123,
        )

    def test_choose_bucket_val_canonical_url_missing_ctx_field(self):
        with create_temp_config_file(self.canonical_url_exp) as f:
            decider = setup_decider_class(f.name)
            ctx = self.valid_ctx_dict.copy()
            del ctx["canonical_url"]

            with self.assertRaises(DeciderException) as e:
                decider.choose("genexp_canonical_url", ctx)
            self.assertEqual(
                str(e.exception),
                'Missing field "canonical_url" in context for bucket_val = canonical_url',
            )

    def test_choose_bucket_val_subreddit_id(self):
        with create_temp_config_file(self.subreddit_id_exp) as f:
            decider = setup_decider_class(f.name)

            choice = decider.choose("genexp_subreddit_id", self.valid_ctx_dict)

            self.assertEqual(
                dict(choice),
                {
                    "variant": "variant_4",
                    "value": None,
                    "feature_id": 123,
                    "feature_name": "genexp_subreddit_id",
                    "feature_version": 5,
                    "events": [
                        f"0::::123::::genexp_subreddit_id::::5::::variant_4::::{SUBREDDIT_ID}::::subreddit_id::::0::::2147483648"
                    ],
                    "full_events": ANY,
                },
            )
            assert len(choice.full_events) == 1
            self.assert_event_json(
                self.valid_ctx_dict,
                choice.full_events[0],
                "subreddit_id",
                "variant_4",
                "genexp_subreddit_id",
                123,
            )

    def test_choose_bucket_val_subreddit_id_missing_ctx_field(self):
        with create_temp_config_file(self.subreddit_id_exp) as f:
            decider = setup_decider_class(f.name)
            ctx = self.valid_ctx_dict.copy()
            del ctx["subreddit_id"]

            with self.assertRaises(DeciderException) as e:
                decider.choose("genexp_subreddit_id", ctx)
            self.assertEqual(
                str(e.exception),
                'Missing field "subreddit_id" in context for bucket_val = subreddit_id',
            )

    def test_choose_bucket_val_ad_account_id(self):
        with create_temp_config_file(self.ad_account_id_exp) as f:
            decider = setup_decider_class(f.name)

            choice = decider.choose("genexp_ad_account_id", self.valid_ctx_dict)

            self.assertEqual(
                dict(choice),
                {
                    "variant": "variant_2",
                    "value": None,
                    "feature_id": 123,
                    "feature_name": "genexp_ad_account_id",
                    "feature_version": 5,
                    "events": [
                        f"0::::123::::genexp_ad_account_id::::5::::variant_2::::{AD_ACCOUNT_ID}::::ad_account_id::::0::::2147483648"
                    ],
                    "full_events": ANY,
                },
            )
            assert len(choice.full_events) == 1
            self.assert_event_json(
                self.valid_ctx_dict,
                choice.full_events[0],
                "ad_account_id",
                "variant_2",
                "genexp_ad_account_id",
                123,
            )

    def test_choose_bucket_val_ad_account_id_missing_ctx_field(self):
        with create_temp_config_file(self.ad_account_id_exp) as f:
            decider = setup_decider_class(f.name)
            ctx = self.valid_ctx_dict.copy()
            del ctx["ad_account_id"]

            with self.assertRaises(DeciderException) as e:
                decider.choose("genexp_ad_account_id", ctx)
            self.assertEqual(
                str(e.exception),
                'Missing field "ad_account_id" in context for bucket_val = ad_account_id',
            )

    def test_choose_bucket_val_business_id(self):
        with create_temp_config_file(self.business_id_exp) as f:
            decider = setup_decider_class(f.name)

            choice = decider.choose("genexp_business_id", self.valid_ctx_dict)

            self.assertEqual(
                dict(choice),
                {
                    "variant": "variant_3",
                    "value": None,
                    "feature_id": 123,
                    "feature_name": "genexp_business_id",
                    "feature_version": 5,
                    "events": [
                        f"0::::123::::genexp_business_id::::5::::variant_3::::{BUSINESS_ID}::::business_id::::0::::2147483648"
                    ],
                    "full_events": ANY,
                },
            )
            assert len(choice.full_events) == 1
            self.assert_event_json(
                self.valid_ctx_dict,
                choice.full_events[0],
                "business_id",
                "variant_3",
                "genexp_business_id",
                123,
            )

    def test_choose_bucket_val_business_id_missing_ctx_field(self):
        with create_temp_config_file(self.business_id_exp) as f:
            decider = setup_decider_class(f.name)
            ctx = self.valid_ctx_dict.copy()
            del ctx["business_id"]

            with self.assertRaises(DeciderException) as e:
                decider.choose("genexp_business_id", ctx)
            self.assertEqual(
                str(e.exception),
                'Missing field "business_id" in context for bucket_val = business_id',
            )

    def test_choose_with_other_fields_for_bucketing(self):
        cfg = self.genexp_0_cfg
        cfg["genexp_0"]["experiment"].update(
            {
                "bucket_val": "foo",
                "variants": [
                    {"range_start": 0.0, "range_end": 1.0, "name": "control_1"},
                ],
            }
        )

        with create_temp_config_file(cfg) as f:
            decider = setup_decider_class(f.name)
            ctx = self.valid_ctx_dict.copy()

            # include bucket_val value in "other_fields"
            ctx.update({"other_fields": {"foo": "bar"}})

            choice = decider.choose("genexp_0", ctx)

            self.assertEqual(
                dict(choice),
                {
                    "variant": "control_1",
                    "value": None,
                    "feature_id": 6299,
                    "feature_name": "genexp_0",
                    "feature_version": 5,
                    "events": [
                        "0::::6299::::genexp_0::::5::::control_1::::bar::::foo::::0::::2147483648"
                    ],
                    "full_events": ANY,
                },
            )
            assert len(choice.full_events) == 1
            self.assert_event_json(
                ctx=ctx,
                event=choice.full_events[0],
                noun="foo",
                variant="control_1",
                bucket_val="bar",
            )

    def test_choose_with_other_fields_for_targeting(self):
        cfg = self.genexp_0_cfg
        cfg["genexp_0"]["experiment"].update(
            {"targeting": {"ALL": [{"EQ": {"field": "foo", "values": ["bar"]}}]}}
        )

        with create_temp_config_file(cfg) as f:
            decider = setup_decider_class(f.name)
            ctx = self.valid_ctx_dict.copy()

            # targeting matches
            ctx.update({"other_fields": {"foo": "bar"}})

            choice = decider.choose("genexp_0", ctx)

            self.assertEqual(
                dict(choice),
                {
                    "variant": "variant_5",
                    "value": None,
                    "feature_id": 6299,
                    "feature_name": "genexp_0",
                    "feature_version": 5,
                    "events": [
                        f"0::::6299::::genexp_0::::5::::variant_5::::{USER_ID}::::user_id::::0::::2147483648"
                    ],
                    "full_events": ANY,
                },
            )
            assert len(choice.full_events) == 1
            self.assert_event_json(
                ctx=ctx,
                event=choice.full_events[0],
                noun="user_id",
                variant="variant_5",
            )

            # targeting doesn't match
            ctx.update({"other_fields": {"foo": "huh"}})

            choice = decider.choose("genexp_0", ctx)
            self.assertEqual(
                dict(choice),
                {
                    "variant": None,
                    "value": None,
                    "feature_id": 6299,
                    "feature_name": "genexp_0",
                    "feature_version": 5,
                    "events": [],
                    "full_events": [],
                },
            )

    def test_choose_with_other_fields_for_overrides(self):
        cfg = self.genexp_0_cfg
        cfg["genexp_0"]["experiment"].update(
            {
                "bucket_val": "foo",
                "overrides": [
                    {
                        "variant_5": {
                            "ANY": [{"EQ": {"field": "foo", "values": ["bar"]}}]
                        }
                    }
                ],
                "variants": [
                    {"range_start": 0.0, "range_end": 0.0, "name": "control_1"},
                    {"range_start": 0.0, "range_end": 0.0, "name": "variant_5"},
                ],
            }
        )

        with create_temp_config_file(cfg) as f:
            decider = setup_decider_class(f.name)
            ctx = self.valid_ctx_dict.copy()

            # override matches
            ctx.update({"other_fields": {"foo": "bar"}})

            choice = decider.choose("genexp_0", ctx)

            self.assertEqual(
                dict(choice),
                {
                    "variant": "variant_5",
                    "value": None,
                    "feature_id": 6299,
                    "feature_name": "genexp_0",
                    "feature_version": 5,
                    "events": [
                        "1::::6299::::genexp_0::::5::::variant_5::::bar::::foo::::0::::2147483648"
                    ],
                    "full_events": ANY,
                },
            )
            assert len(choice.full_events) == 1
            self.assert_event_json(
                ctx=ctx,
                event=choice.full_events[0],
                noun="foo",
                variant="variant_5",
                decision_kind="Override",
                bucket_val="bar",
                is_override=True,
            )

            # override doesn't match
            ctx.update({"other_fields": {"foo": "huh"}})

            choice = decider.choose("genexp_0", ctx)
            self.assertEqual(
                dict(choice),
                {
                    "variant": None,
                    "value": None,
                    "feature_id": 6299,
                    "feature_name": "genexp_0",
                    "feature_version": 5,
                    "events": [],
                    "full_events": [],
                },
            )

    def test_choose_feature_not_found(self):
        with test_feature_not_found() as d:
            with self.assertRaises(FeatureNotFoundException) as e:
                d.choose("any", self.valid_ctx_dict)

            self.assertEqual(
                str(e.exception),
                'Feature "any" not found.',
            )

    def test_choose_with_a_value(self):
        cfg = {
            "dc_bool": {
                "id": 3393,
                "value": True,
                "type": "dynamic_config",
                "version": "2",
                "enabled": True,
                "name": "dc_bool",
                "value_type": "Boolean",
                "experiment": {"experiment_version": 2},
            }
        }
        with create_temp_config_file(cfg) as f:
            decider = setup_decider_class(f.name)

            choice = decider.choose("dc_bool", self.valid_ctx_dict)

            self.assertEqual(
                dict(choice),
                {
                    "variant": None,
                    "value": True,
                    "feature_id": 3393,
                    "feature_name": "dc_bool",
                    "feature_version": 2,
                    "events": [],
                    "full_events": [],
                },
            )

    def test_measured_rollouts(self):
        configs = json.load(open(f"{TEST_DIR}/../../test.json"))

        cfg = {
            "feature_rollout_100": configs["feature_rollout_100"],
            "measured_rollout_100": configs["measured_rollout_100"],
        }

        with create_temp_config_file(cfg) as f:
            decider = setup_decider_class(f.name)

            choice = decider.choose("feature_rollout_100", self.valid_ctx_dict)

            self.assertEqual(
                dict(choice),
                {
                    "variant": "enabled",
                    "value": None,
                    "feature_id": 9110,
                    "feature_name": "feature_rollout_100",
                    "feature_version": 1,
                    # FR doesn't emit events (due to `emit_event: false``)
                    "events": [],
                    "full_events": [],
                },
            )

            choice = decider.choose("measured_rollout_100", self.valid_ctx_dict)

            self.assertEqual(
                dict(choice),
                {
                    "variant": "enabled",
                    "value": None,
                    "feature_id": 9119,
                    "feature_name": "measured_rollout_100",
                    "feature_version": 1,
                    # MR emits event
                    "events": [
                        f"0::::9119::::measured_rollout_100::::1::::enabled::::{USER_ID}::::user_id::::1522306800::::32533405261"
                    ],
                    "full_events": ANY,
                },
            )

            # MR sets "measured" to True
            mr_feature = decider.get_feature("measured_rollout_100")
            self.assertEqual(mr_feature.measured, True)

    def test_choose_all(self):
        self.genexp_0_cfg.update(self.additional_2_exp)

        with create_temp_config_file(self.genexp_0_cfg) as f:
            decider = setup_decider_class(f.name)

            decisions = decider.choose_all(self.valid_ctx_dict)

        # all experiments are returned
        # including "exp_1", which has 0% bucketing ("variant": None)
        self.assertEqual(len(decisions), 3)

        # assert genexp_0
        self.assertEqual(
            dict(decisions["genexp_0"]),
            {
                "variant": "variant_5",
                "value": None,
                "feature_version": 5,
                "feature_id": 6299,
                "feature_name": "genexp_0",
                "events": [
                    f"0::::6299::::genexp_0::::5::::variant_5::::{USER_ID}::::user_id::::0::::2147483648"
                ],
                "full_events": ANY,
            },
        )
        assert len(decisions["genexp_0"].full_events) == 1
        self.assert_event_json(
            ctx=self.valid_ctx_dict,
            event=decisions["genexp_0"].full_events[0],
            noun="user_id",
            variant="variant_5",
        )

        # assert exp_0
        self.assertEqual(
            dict(decisions["exp_0"]),
            {
                "variant": "variant_3",
                "value": None,
                "feature_version": 5,
                "feature_id": 3248,
                "feature_name": "exp_0",
                "events": [
                    f"0::::3248::::exp_0::::5::::variant_3::::{USER_ID}::::user_id::::37173982::::2147483648"
                ],
                "full_events": ANY,
            },
        )

        assert len(decisions["exp_0"].full_events) == 1
        self.assert_event_json(
            ctx=self.valid_ctx_dict,
            event=decisions["exp_0"].full_events[0],
            noun="user_id",
            variant="variant_3",
            experiment_name="exp_0",
            experiment_id=3248,
        )

        # assert exp_1 is included even though "variant" is `None`
        self.assertEqual(
            dict(decisions["exp_1"]),
            {
                "variant": None,
                "value": None,
                "feature_version": 5,
                "feature_id": 3246,
                "feature_name": "exp_1",
                "events": [],
                "full_events": [],
            },
        )

    def test_choose_all_without_ctx(self):
        with create_temp_config_file(self.genexp_0_cfg) as f:
            decider = setup_decider_class(f.name)

            with self.assertRaises(DeciderException) as e:
                decider.choose_all(None)

        self.assertEqual(
            str(e.exception),
            "Missing `context` param",
        )

    def test_choose_all_with_single_identifier_type(self):
        self.genexp_0_cfg.update(self.additional_2_exp)
        self.genexp_0_cfg.update(self.canonical_url_exp)

        with create_temp_config_file(self.genexp_0_cfg) as f:
            decider = setup_decider_class(f.name)

            decisions = decider.choose_all(
                context=self.valid_ctx_dict, bucketing_field_filter="canonical_url"
            )

        # assert canonical_url_exp
        self.assertEqual(len(decisions), 1)
        self.assertEqual(
            dict(decisions["genexp_canonical_url"]),
            {
                "variant": "variant_3",
                "value": None,
                "feature_version": 5,
                "feature_id": 123,
                "feature_name": "genexp_canonical_url",
                "events": [
                    f"0::::123::::genexp_canonical_url::::5::::variant_3::::{CANONICAL_URL}::::canonical_url::::0::::2147483648"
                ],
                "full_events": ANY,
            },
        )
        assert len(decisions["genexp_canonical_url"].full_events) == 1
        self.assert_event_json(
            ctx=self.valid_ctx_dict,
            event=decisions["genexp_canonical_url"].full_events[0],
            noun="canonical_url",
            variant="variant_3",
            experiment_name="genexp_canonical_url",
            experiment_id=123,
        )

    def test_choose_all_bucket_val_device_id_missing_identifier(self):
        # 3 exp total
        # 1 of which is a device_id exp
        self.device_id_exp.update(self.additional_2_exp)

        with create_temp_config_file(self.device_id_exp) as f:
            decider = setup_decider_class(f.name)
            ctx = self.valid_ctx_dict.copy()
            del ctx["device_id"]

            decisions = decider.choose_all(ctx)

        # device_id exp is excluded from return value
        # since it failed bucketing due to missing "device_id" in context
        self.assertEqual(len(decisions), 2)

        # assert exp_0
        self.assertEqual(
            dict(decisions["exp_0"]),
            {
                "variant": "variant_3",
                "value": None,
                "feature_version": 5,
                "feature_id": 3248,
                "feature_name": "exp_0",
                "events": [
                    f"0::::3248::::exp_0::::5::::variant_3::::{USER_ID}::::user_id::::37173982::::2147483648"
                ],
                "full_events": ANY,
            },
        )

        assert len(decisions["exp_0"].full_events) == 1
        self.assert_event_json(
            ctx=ctx,
            event=decisions["exp_0"].full_events[0],
            noun="user_id",
            variant="variant_3",
            experiment_name="exp_0",
            experiment_id=3248,
        )

        # assert exp_1 is included even though "variant" is `None`
        self.assertEqual(
            dict(decisions["exp_1"]),
            {
                "variant": None,
                "value": None,
                "feature_version": 5,
                "feature_id": 3246,
                "feature_name": "exp_1",
                "events": [],
                "full_events": [],
            },
        )

    def test_get_feature(self):
        with create_temp_config_file(self.genexp_0_cfg) as f:
            decider = setup_decider_class(f.name)

            feature = decider.get_feature("genexp_0")

            cfg = self.genexp_0_cfg["genexp_0"]
            self.assertEqual(feature.id, cfg["id"])
            self.assertEqual(feature.name, cfg["name"])
            self.assertEqual(feature.version, cfg["experiment"]["experiment_version"])
            self.assertEqual(feature.bucket_val, cfg["experiment"]["bucket_val"])
            self.assertEqual(feature.start_ts, cfg["start_ts"])
            self.assertEqual(feature.stop_ts, cfg["stop_ts"])
            self.assertEqual(feature.emit_event, True)
            self.assertEqual(feature.measured, False)

            self.assertEqual(
                dict(feature),
                {
                    "id": cfg["id"],
                    "name": cfg["name"],
                    "version": cfg["experiment"]["experiment_version"],
                    "bucket_val": cfg["experiment"]["bucket_val"],
                    "start_ts": cfg["start_ts"],
                    "stop_ts": cfg["stop_ts"],
                    "emit_event": True,
                    "measured": False,
                },
            )

    def test_get_feature_does_not_exist(self):
        with test_feature_not_found() as d:
            with self.assertRaises(FeatureNotFoundException) as e:
                d.get_feature("any")

            self.assertEqual(
                str(e.exception),
                'Feature "any" not found.',
            )

    def test_version(self):
        release_version = json.load(
            open(f"{TEST_DIR}/../../.release-please-manifest.json")
        )["."]
        v = version()
        version_check = v == "0.0.1-dev" or v == release_version
        self.assertEqual(version_check, True)

        with create_temp_config_file(self.genexp_0_cfg) as f:
            decider = setup_decider_class(f.name)
            decider_version_check = (
                decider._pkg_version == release_version
                or decider._pkg_version == "0.0.1-dev"
            )
            self.assertEqual(decider_version_check, True)


class TestDeciderGetDynamicConfig(TestCase):
    def setUp(self):
        super().setUp()

        self.valid_ctx_dict = ctx_dict
        self.dc_base_config = {
            "dc_1": {
                "id": 1,
                "name": "dc_1",
                "enabled": True,
                "version": "1",
                "type": "dynamic_config",
                "start_ts": 37173982,
                "stop_ts": 2147483648,
                "owner": "test_owner",
                "experiment": {
                    "experiment_version": 1,
                },
            }
        }

    def test_get_bool(self):
        bool_val = True
        self.dc_base_config["dc_1"].update({"value_type": "Boolean", "value": bool_val})

        with create_temp_config_file(self.dc_base_config) as f:
            decider = setup_decider_class(f.name)
            res = decider.get_bool("dc_1", {})
            self.assertEqual(res, bool_val)

            # test type mismatch
            with self.assertRaises(ValueTypeMismatchException) as e:
                decider.get_float("dc_1", {})

            self.assertEqual(
                str(e.exception),
                'Feature "dc_1" not of float type.',
            )

    def test_get_feature_does_not_exist(self):
        with test_feature_not_found() as d:
            with self.assertRaises(FeatureNotFoundException) as e:
                d.get_bool("any", {})

            self.assertEqual(
                str(e.exception),
                'Feature "any" not found.',
            )

    def test_get_bool_missing_ctx(self):
        bool_val = True
        self.dc_base_config["dc_1"].update({"value_type": "Boolean", "value": bool_val})

        with create_temp_config_file(self.dc_base_config) as f:
            decider = setup_decider_class(f.name)
            with self.assertRaises(DeciderException) as e:
                decider.get_bool("dc_1", None)

            self.assertEqual(
                str(e.exception),
                "Missing `context` param for feature_name: dc_1",
            )

    def test_get_int(self):
        int_val = 7
        self.dc_base_config["dc_1"].update({"value_type": "Integer", "value": int_val})

        with create_temp_config_file(self.dc_base_config) as f:
            decider = setup_decider_class(f.name)

            res = decider.get_int("dc_1", {})
            self.assertEqual(res, int_val)

            # test type mismatch
            with self.assertRaises(ValueTypeMismatchException) as e:
                decider.get_bool("dc_1", {})

            self.assertEqual(
                str(e.exception),
                'Feature "dc_1" not of boolean type.',
            )

    def test_get_float(self):
        float_val = 4.20
        self.dc_base_config["dc_1"].update({"value_type": "Float", "value": float_val})

        with create_temp_config_file(self.dc_base_config) as f:
            decider = setup_decider_class(f.name)

            res = decider.get_float("dc_1", {})
            self.assertEqual(res, float_val)

            # test type mismatch
            with self.assertRaises(ValueTypeMismatchException) as e:
                decider.get_map("dc_1", {})

            self.assertEqual(
                str(e.exception),
                'Feature "dc_1" not of map type.',
            )

    def test_get_string(self):
        string_val = "helloworld!"
        self.dc_base_config["dc_1"].update({"value_type": "Text", "value": string_val})

        with create_temp_config_file(self.dc_base_config) as f:
            decider = setup_decider_class(f.name)

            res = decider.get_string("dc_1", {})
            self.assertEqual(res, string_val)

            # test type mismatch
            with self.assertRaises(ValueTypeMismatchException) as e:
                decider.get_int("dc_1", {})

            self.assertEqual(
                str(e.exception),
                'Feature "dc_1" not of integer type.',
            )

    def test_get_map(self):
        map_val = {
            "v": {"nested_map": {"w": False, "x": 1, "y": "some_string", "z": 3.0}},
            "w": False,
            "x": 1,
            "y": "some_string",
            "z": 3.0,
        }
        self.dc_base_config["dc_1"].update({"value_type": "Map", "value": map_val})

        with create_temp_config_file(self.dc_base_config) as f:
            decider = setup_decider_class(f.name)

            res = decider.get_map("dc_1", {})
            self.assertEqual(res, map_val)

            # test type mismatch
            with self.assertRaises(ValueTypeMismatchException) as e:
                decider.get_string("dc_1", {})

            self.assertEqual(
                str(e.exception),
                'Feature "dc_1" not of string type.',
            )

    def test_get_all_values(self):
        base_cfg = self.dc_base_config["dc_1"].copy()

        bool_val = True
        cfg_bool = {"dc_bool": base_cfg.copy()}
        cfg_bool["dc_bool"].update(
            {"name": "dc_bool", "value": bool_val, "value_type": "Boolean"}
        )

        cfg_missing_bool = {}
        cfg_missing_bool["dc_missing_bool"] = cfg_bool["dc_bool"].copy()
        cfg_missing_bool["dc_missing_bool"].update(
            {"value": None, "name": "dc_missing_bool"}
        )

        int_val = 99
        cfg_int = {"dc_int": base_cfg.copy()}
        cfg_int["dc_int"].update(
            {"name": "dc_int", "value": int_val, "value_type": "Integer"}
        )

        cfg_missing_int = {}
        cfg_missing_int["dc_missing_int"] = cfg_int["dc_int"].copy()
        cfg_missing_int["dc_missing_int"].update(
            {"value": None, "name": "dc_missing_int"}
        )

        float_val = 3.2
        cfg_float = {"dc_float": base_cfg.copy()}
        cfg_float["dc_float"].update(
            {"name": "dc_float", "value": float_val, "value_type": "Float"}
        )

        cfg_missing_float = {}
        cfg_missing_float["dc_missing_float"] = cfg_float["dc_float"].copy()
        cfg_missing_float["dc_missing_float"].update(
            {"value": None, "name": "dc_missing_float"}
        )

        string_val = "some_string"
        cfg_string = {"dc_string": base_cfg.copy()}
        cfg_string["dc_string"].update(
            {"name": "dc_string", "value": string_val, "value_type": "String"}
        )
        cfg_text = {"dc_text": base_cfg.copy()}
        cfg_text["dc_text"].update(
            {"name": "dc_text", "value": string_val, "value_type": "Text"}
        )

        cfg_missing_string = {}
        cfg_missing_string["dc_missing_string"] = cfg_string["dc_string"].copy()
        cfg_missing_string["dc_missing_string"].update(
            {"value": None, "name": "dc_missing_string"}
        )

        cfg_missing_text = {}
        cfg_missing_text["dc_missing_text"] = cfg_text["dc_text"].copy()
        cfg_missing_text["dc_missing_text"].update(
            {"value": None, "name": "dc_missing_text"}
        )

        map_val = {
            "v": {"nested_map": {"w": True, "x": 1, "y": "some_string", "z": 3.0}},
            "w": False,
            "x": 1,
            "y": "some_string",
            "z": 3.0,
        }
        cfg_map = {"dc_map": base_cfg.copy()}
        cfg_map["dc_map"].update(
            {"name": "dc_map", "value": map_val, "value_type": "Map"}
        )

        cfg_missing_map = {}
        cfg_missing_map["dc_missing_map"] = cfg_map["dc_map"].copy()
        cfg_missing_map["dc_missing_map"].update(
            {"value": None, "name": "dc_missing_map"}
        )

        missing_value_type_cfg = {
            "dc_missing_value_type": {
                "id": 3393,
                "value": False,
                "type": "dynamic_config",
                "version": "2",
                "enabled": True,
                "name": "dc_missing_value_type",
                "experiment": {"experiment_version": 2},
            }
        }

        experiments_cfg = {
            "genexp_0": {
                "id": 6299,
                "name": "genexp_0",
                "enabled": True,
                "version": "5",
                "emit_event": True,
                "type": "range_variant",
                "start_ts": 0,
                "stop_ts": 2147483648,
                "experiment": {
                    "variants": [
                        {"range_start": 0.0, "range_end": 0.2, "name": "control_1"},
                        {"range_start": 0.2, "range_end": 0.4, "name": "variant_2"},
                        {"range_start": 0.4, "range_end": 0.6, "name": "variant_3"},
                        {"range_start": 0.6, "range_end": 0.8, "name": "variant_4"},
                        {"range_start": 0.8, "range_end": 1.0, "name": "variant_5"},
                    ],
                    "experiment_version": 5,
                    "shuffle_version": 91,
                    "bucket_val": "user_id",
                    "log_bucketing": False,
                },
            },
            "exp_0": {
                "id": 3248,
                "name": "exp_0",
                "enabled": True,
                "version": "5",
                "type": "range_variant",
                "emit_event": True,
                "start_ts": 37173982,
                "stop_ts": 2147483648,
                "experiment": {
                    "variants": [
                        {"range_start": 0.0, "range_end": 0.2, "name": "control_1"},
                        {"range_start": 0.2, "range_end": 0.4, "name": "control_2"},
                        {"range_start": 0.4, "range_end": 0.6, "name": "variant_2"},
                        {"range_start": 0.6, "range_end": 0.8, "name": "variant_3"},
                        {"range_start": 0.8, "range_end": 1.0, "name": "variant_4"},
                    ],
                    "experiment_version": 2,
                    "shuffle_version": 91,
                    "bucket_val": "user_id",
                    "log_bucketing": False,
                },
            },
            "exp_1": {
                "id": 3246,
                "name": "exp_1",
                "enabled": True,
                "version": "5",
                "type": "range_variant",
                "emit_event": True,
                "start_ts": 37173982,
                "stop_ts": 2147483648,
                "experiment": {
                    "variants": [
                        {"range_start": 0, "range_end": 0, "name": "variant_0"}
                    ],
                    "experiment_version": 2,
                    "shuffle_version": 0,
                    "bucket_val": "user_id",
                    "log_bucketing": False,
                },
            },
        }
        experiments_cfg.update(cfg_bool)
        experiments_cfg.update(cfg_int)
        experiments_cfg.update(cfg_float)
        experiments_cfg.update(cfg_string)
        experiments_cfg.update(cfg_text)
        experiments_cfg.update(cfg_map)

        # should be set to default values
        experiments_cfg.update(cfg_missing_bool)
        experiments_cfg.update(cfg_missing_int)
        experiments_cfg.update(cfg_missing_float)
        experiments_cfg.update(cfg_missing_string)
        experiments_cfg.update(cfg_missing_text)
        experiments_cfg.update(cfg_missing_map)

        # missing "value_type" field
        experiments_cfg.update(missing_value_type_cfg)

        with create_temp_config_file(experiments_cfg) as f:
            decider = setup_decider_class(f.name)

            configs = decider.all_values({})

            # 6 correct DCs, 6 DCs w/ values set to respective defaults
            # 1 `missing_value_type_cfg` which sets "type" to empty string
            # (3 regular experiments are excluded)
            self.assertEqual(len(configs), 13)

            # test values get set
            self.assertEqual(configs["dc_bool"], bool_val)

            self.assertEqual(configs["dc_int"], int_val)

            self.assertEqual(configs["dc_float"], float_val)

            self.assertEqual(configs["dc_string"], string_val)

            self.assertEqual(configs["dc_text"], string_val)

            self.assertEqual(configs["dc_map"], map_val)

            # test default values
            self.assertEqual(configs["dc_missing_bool"], False)

            self.assertEqual(configs["dc_missing_int"], 0)

            self.assertEqual(configs["dc_missing_float"], 0.0)

            self.assertEqual(configs["dc_missing_string"], "")

            self.assertEqual(configs["dc_missing_text"], "")

            self.assertEqual(configs["dc_missing_map"], {})

            # set "type" to empty string if "value_type" is missing on cfg
            self.assertEqual(configs["dc_missing_value_type"], False)
