@extends('layouts.app')

@section('title', 'Services - Vibe Coding Portal')

@section('content')
<div class="container">
    <div class="text-center mb-5">
        <span class="badge bg-success px-3 py-2 mb-2">Our Modules</span>
        <h1 class="display-6 fw-bold">Practicals & Technology Stack</h1>
        <p class="text-muted">Explore the core competencies developed through this course</p>
    </div>

    <div class="row g-4">
        <div class="col-md-4">
            <div class="card h-100 border-0 shadow-sm p-3">
                <div class="card-body">
                    <i class="bi bi-code-slash text-primary mb-3" style="font-size: 2rem;"></i>
                    <h5 class="fw-bold">AI Pair Programming</h5>
                    <p class="text-secondary small">Vibe coding with LLMs, code generation, refactoring, and AI-driven debugging.</p>
                </div>
            </div>
        </div>
        <div class="col-md-4">
            <div class="card h-100 border-0 shadow-sm p-3">
                <div class="card-body">
                    <i class="bi bi-layers-fill text-danger mb-3" style="font-size: 2rem;"></i>
                    <h5 class="fw-bold">Laravel MVC Framework</h5>
                    <p class="text-secondary small">Routing, Blade layouts, Eloquent ORM, migrations, and robust CRUD architectures.</p>
                </div>
            </div>
        </div>
        <div class="col-md-4">
            <div class="card h-100 border-0 shadow-sm p-3">
                <div class="card-body">
                    <i class="bi bi-window-desktop text-success mb-3" style="font-size: 2rem;"></i>
                    <h5 class="fw-bold">Python GUI & SQLite</h5>
                    <p class="text-secondary small">Desktop GUI applications with Tkinter, event-handling, and relational SQLite databases.</p>
                </div>
            </div>
        </div>
    </div>
</div>
@endsection
