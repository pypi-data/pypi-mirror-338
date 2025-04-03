use criterion::{Criterion, criterion_group, criterion_main};

fn criterion_benchmark(c: &mut Criterion) {
    c.bench_function("c2k", |b| {
        let c2k = kanalizer::C2k::new();
        b.iter(|| std::hint::black_box(c2k.infer("kanalizer")))
    });
}

criterion_group!(benches, criterion_benchmark);
criterion_main!(benches);
