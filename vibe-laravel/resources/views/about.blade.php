@extends('layouts.app')

@section('title', 'About Us - Vibe Coding Portal')

@section('content')
<div class="container">
    <div class="row align-items-center mb-5">
        <div class="col-lg-7">
            <span class="badge bg-primary px-3 py-2 mb-2">About Our Lab</span>
            <h1 class="display-6 fw-bold text-dark mb-3">About Vibe Coding & Application Design</h1>
            <p class="lead text-secondary">
                This course (DI05000121) introduces modern AI-assisted engineering practices, moving developers from line-by-line syntax drafting to intent-driven architecture and rapid prototyping.
            </p>
            <div class="p-3 bg-white rounded-3 shadow-sm border-start border-4 border-primary mt-4">
                <h5 class="fw-bold mb-1">Semester 5 - Computer Engineering</h5>
                <p class="mb-0 text-muted">Government Polytechnic College, Jamnagar (GTU Affiliated)</p>
            </div>
        </div>
        <div class="col-lg-5 text-center mt-4 mt-lg-0">
            <div class="p-5 bg-white shadow-sm rounded-4 border">
                <i class="bi bi-mortarboard-fill text-primary" style="font-size: 5rem;"></i>
                <h4 class="fw-bold mt-3">Skill-Driven Learning</h4>
                <p class="text-secondary small">Hands-on practical exploration with Laravel, Python, Git, and AI assistants.</p>
            </div>
        </div>
    </div>
</div>
@endsection
