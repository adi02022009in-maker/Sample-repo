@extends('layouts.app')

@section('title', 'Responsive Interface - Bootstrap 5')

@section('content')
<div class="container">

    <!-- Responsive Hero Section -->
    <div class="hero-banner p-4 p-md-5 mb-5 shadow text-center text-md-start">
        <div class="row align-items-center">
            <div class="col-lg-8">
                <span class="badge bg-warning text-dark px-3 py-2 mb-3 fw-bold">Bootstrap 5 Responsive Grid</span>
                <h1 class="display-5 fw-bold mb-3">Modern & Responsive Web Design</h1>
                <p class="lead mb-4">
                    Built with HTML5, CSS3, and Bootstrap 5 in Laravel Blade. This layout dynamically adapts to mobile screens, tablets, and desktop displays.
                </p>
                <div class="d-flex flex-column flex-sm-row gap-2 justify-content-center justify-content-md-start">
                    <a href="#features" class="btn btn-light btn-lg px-4 fw-semibold shadow-sm">Explore Cards</a>
                    <a href="#about" class="btn btn-outline-light btn-lg px-4">Learn More</a>
                </div>
            </div>
            <div class="col-lg-4 text-center mt-4 mt-lg-0">
                <i class="bi bi-phone-flip text-light" style="font-size: 7rem; opacity: 0.9;"></i>
            </div>
        </div>
    </div>

    <!-- Responsive 3-Column Grid Section -->
    <div id="features" class="mb-5">
        <div class="text-center mb-4">
            <h2 class="fw-bold">Responsive Grid System</h2>
            <p class="text-muted">Columns automatically rearrange on different screen viewports</p>
        </div>

        <div class="row g-4">
            <!-- Column 1: Mobile (12), Tablet (6), Desktop (4) -->
            <div class="col-12 col-md-6 col-lg-4">
                <div class="card h-100 border-0 shadow-sm feature-card p-3">
                    <div class="card-body">
                        <div class="text-primary mb-3">
                            <i class="bi bi-phone" style="font-size: 2.2rem;"></i>
                        </div>
                        <h5 class="card-title fw-bold">Mobile Viewport</h5>
                        <p class="card-text text-secondary">
                            On small mobile devices (&lt; 768px), each card expands to full 100% width using <code>col-12</code> for optimal tap usability.
                        </p>
                        <span class="badge bg-primary-subtle text-primary border border-primary-subtle">col-12</span>
                    </div>
                </div>
            </div>

            <!-- Column 2: Mobile (12), Tablet (6), Desktop (4) -->
            <div class="col-12 col-md-6 col-lg-4">
                <div class="card h-100 border-0 shadow-sm feature-card p-3">
                    <div class="card-body">
                        <div class="text-success mb-3">
                            <i class="bi bi-tablet" style="font-size: 2.2rem;"></i>
                        </div>
                        <h5 class="card-title fw-bold">Tablet Viewport</h5>
                        <p class="card-text text-secondary">
                            On medium tablet screens (&ge; 768px), cards rearrange into a comfortable 2-column layout using <code>col-md-6</code>.
                        </p>
                        <span class="badge bg-success-subtle text-success border border-success-subtle">col-md-6</span>
                    </div>
                </div>
            </div>

            <!-- Column 3: Mobile (12), Tablet (6), Desktop (4) -->
            <div class="col-12 col-md-6 col-lg-4">
                <div class="card h-100 border-0 shadow-sm feature-card p-3">
                    <div class="card-body">
                        <div class="text-warning mb-3">
                            <i class="bi bi-laptop" style="font-size: 2.2rem;"></i>
                        </div>
                        <h5 class="card-title fw-bold">Desktop Viewport</h5>
                        <p class="card-text text-secondary">
                            On large desktop monitors (&ge; 992px), cards display in a 3-column layout using <code>col-lg-4</code> side-by-side.
                        </p>
                        <span class="badge bg-warning-subtle text-warning border border-warning-subtle">col-lg-4</span>
                    </div>
                </div>
            </div>
        </div>
    </div>

</div>
@endsection
