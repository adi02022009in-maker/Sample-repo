@extends('layouts.app')

@section('title', 'Librarian Login - Vibe Library')

@section('content')
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-5">
            <div class="card border-0 shadow-sm rounded-3">
                <div class="card-header bg-dark text-white py-3 text-center">
                    <h5 class="mb-0 fw-bold"><i class="bi bi-shield-lock-fill me-2 text-warning"></i>User Authentication</h5>
                    <small class="text-secondary">Library Management System</small>
                </div>
                <div class="card-body p-4">
                    @if ($errors->any())
                        <div class="alert alert-danger py-2 mb-3">
                            <small>{{ $errors->first() }}</small>
                        </div>
                    @endif

                    <form action="{{ route('login.post') }}" method="POST">
                        @csrf
                        <div class="mb-3">
                            <label class="form-label fw-semibold">Email Address</label>
                            <input type="email" name="email" class="form-control" value="admin@library.com" required>
                        </div>
                        <div class="mb-3">
                            <label class="form-label fw-semibold">Password</label>
                            <input type="password" name="password" class="form-control" value="password123" required>
                            <small class="text-muted">Demo Credentials: admin@library.com / password123</small>
                        </div>
                        <button type="submit" class="btn btn-primary w-100 fw-bold py-2">
                            <i class="bi bi-box-arrow-in-right me-1"></i>Login to System
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
@endsection
