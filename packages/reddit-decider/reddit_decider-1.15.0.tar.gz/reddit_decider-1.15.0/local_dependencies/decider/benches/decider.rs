use criterion::measurement::WallTime;
use criterion::{
    black_box, criterion_group, criterion_main, BenchmarkGroup, BenchmarkId, Criterion, Throughput,
};
use std::collections::HashMap;
use std::path::PathBuf;

use decider::{Context, ContextField, Decider};

fn resource_path(file: &str) -> String {
    let mut dir = PathBuf::from(env!("CARGO_MANIFEST_DIR"));
    dir.pop();
    dir.push(file);

    dir.to_str().unwrap().to_string()
}

pub fn bench_dynamic_config(c: &mut Criterion) {
    let mut group = c.benchmark_group("Dynamic Config");
    group.throughput(Throughput::Elements(1));

    let decider = Decider::new(resource_path("bench_cfg.json")).unwrap();
    let ctx = Context::default();

    group.bench_function("get_bool", |b| {
        b.iter(|| {
            decider
                .get_bool(black_box("dc_bool"), black_box(&ctx))
                .unwrap()
        })
    });

    group.bench_function("get_int", |b| {
        b.iter(|| {
            decider
                .get_int(black_box("dc_int"), black_box(&ctx))
                .unwrap()
        })
    });

    group.bench_function("get_float", |b| {
        b.iter(|| {
            decider
                .get_float(black_box("dc_float"), black_box(&ctx))
                .unwrap()
        })
    });

    group.bench_function("get_string", |b| {
        b.iter(|| {
            decider
                .get_string(black_box("dc_string"), black_box(&ctx))
                .unwrap()
        })
    });

    group.bench_function("get_map", |b| {
        b.iter(|| {
            decider
                .get_map(black_box("dc_map"), black_box(&ctx))
                .unwrap()
        })
    });

    group.bench_function("get_all_values", |b| {
        b.iter(|| decider.get_all_values(black_box(&ctx)).unwrap())
    });

    group.finish()
}

pub fn bench_choose(c: &mut Criterion) {
    let mut group = c.benchmark_group("choose");
    group.throughput(Throughput::Elements(1));

    let decider = Decider::new(resource_path("bench_cfg.json")).unwrap();
    let ctx = Context::default();

    group.bench_function("darkmode", |b| {
        b.iter(|| {
            decider
                .choose(black_box("exp_dark"), black_box(&ctx), None)
                .unwrap()
        })
    });

    bench_fractional_availability(&mut group, &decider);
    bench_override(&mut group, &decider);
    bench_targeting(&mut group, &decider);

    bench_holdout_mutex_groups(&mut group, &decider);

    group.finish()
}

fn bench_fractional_availability(group: &mut BenchmarkGroup<WallTime>, decider: &Decider) {
    let ctx = Context {
        user_id: Some("0".to_string()),

        ..Context::default()
    };

    group.bench_function("fractional_availability", |b| {
        b.iter(|| {
            decider
                .choose(black_box("exp_0"), black_box(&ctx), None)
                .unwrap()
        })
    });
}

fn bench_override(group: &mut BenchmarkGroup<WallTime>, decider: &Decider) {
    let override_ctx = Context {
        user_id: Some("1".to_string()),
        ..Context::default()
    };

    group.bench_function("override/overridden ctx", |b| {
        b.iter(|| {
            decider
                .choose(black_box("exp_override"), black_box(&override_ctx), None)
                .unwrap()
        })
    });

    let mut regular_ctx = override_ctx.clone();
    regular_ctx.user_id = Some("2".to_string());

    group.bench_function("override/non-overridden ctx", |b| {
        b.iter(|| {
            decider
                .choose(black_box("exp_override"), black_box(&regular_ctx), None)
                .unwrap()
        })
    });
}

fn bench_targeting(group: &mut BenchmarkGroup<WallTime>, decider: &Decider) {
    let targeted_ctx = Context {
        user_id: Some("1000".to_string()),
        country_code: Some("1000".to_string()),
        app_name: Some("android".to_string()),
        ..Context::default()
    };

    group.bench_function("targeting/targeted ctx", |b| {
        b.iter(|| {
            decider
                .choose(black_box("x0"), black_box(&targeted_ctx), None)
                .unwrap()
        })
    });

    let mut untargeted_ctx = targeted_ctx.clone();
    untargeted_ctx.app_name = Some("ios".to_string());

    group.bench_function("targeting/untargeted ctx", |b| {
        b.iter(|| {
            decider
                .choose(black_box("x0"), black_box(&untargeted_ctx), None)
                .unwrap()
        })
    });
}

fn bench_holdout_mutex_groups(group: &mut BenchmarkGroup<WallTime>, decider: &Decider) {
    let user_ids = HashMap::from([
        ("holdout", Some("0".to_string())),
        ("no bucket", Some("8".to_string())),
        ("control", Some("4".to_string())),
    ]);

    for (tag, user_id) in user_ids {
        let ctx = Context {
            user_id,
            ..Context::default()
        };

        group.bench_function(BenchmarkId::new("holdout", tag), |b| {
            b.iter(|| {
                decider
                    .choose(black_box("e1"), black_box(&ctx), None)
                    .unwrap()
            })
        });
    }
}

pub fn bench_choose_all(c: &mut Criterion) {
    let mut group = c.benchmark_group("choose");
    group.throughput(Throughput::Elements(1));

    let decider = Decider::new(resource_path("bench_cfg.json")).unwrap();
    let ctx = Context::default();

    for (bv_str, bv) in vec![
        ("none", None),
        ("user_id", Some(ContextField::UserId)),
        ("device_id", Some(ContextField::DeviceId)),
        ("canonical_url", Some(ContextField::CanonicalUrl)),
    ]
    .into_iter()
    {
        group.bench_function(format!("choose_all/bv_override_{}", bv_str), |b| {
            b.iter(|| decider.choose_all(black_box(&ctx), black_box(bv.clone())))
        });
    }
}

criterion_group!(
    benches,
    bench_dynamic_config,
    bench_choose,
    bench_choose_all
);
criterion_main!(benches);
