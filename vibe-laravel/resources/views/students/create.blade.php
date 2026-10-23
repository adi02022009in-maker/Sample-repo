@extends('layouts.app')

@section('title', 'Register New Student - Vibe Coding')

@section('content')
<div class="container">
    <div class="row justify-content-center">
        <div class="col-lg-7">
            <div class="card border-0 shadow-sm rounded-3">
                <div class="card-header bg-primary text-white py-3">
                    <h5 class="card-title mb-0 fw-bold">
                        <i class="bi bi-person-plus-fill me-2"></i>Student Registration Form
                    </h5>
                </div>
                <div class="card-body p-4">

                    <!-- Validation Errors Banner -->
                    @if ($errors->any())
                        <div class="alert alert-danger mb-4">
                            <ul class="mb-0">
                                @foreach ($errors->all() as $error)
                                    <li>{{ $error }}</li>
                                @endforeach
                            </ul>
                        </div>
                    @endif

                    <form action="{{ route('students.store') }}" method="POST">
                        @csrf

                        <!-- Full Name -->
                        <div class="mb-3">
                            <label class="form-label fw-semibold">Full Name</label>
                            <input type="text" name="name" class="form-control @error('name') is-invalid @enderror" value="{{ old('name') }}" placeholder="e.g. Rahul Sharma" required>
                            @error('name')
                                <div class="invalid-feedback">{{ $message }}</div>
                            @enderror
                        </div>

                        <!-- Email Address -->
                        <div class="mb-3">
                            <label class="form-label fw-semibold">Email Address</label>
                            <input type="email" name="email" class="form-control @error('email') is-invalid @enderror" value="{{ old('email') }}" placeholder="e.g. rahul@example.com" required>
                            @error('email')
                                <div class="invalid-feedback">{{ $message }}</div>
                            @enderror
                        </div>

                        <!-- Enrollment Number -->
                        <div class="mb-3">
                            <label class="form-label fw-semibold">Enrollment Number</label>
                            <input type="text" name="enrollment_no" class="form-control @error('enrollment_no') is-invalid @enderror" value="{{ old('enrollment_no') }}" placeholder="e.g. 246250307086" required>
                            @error('enrollment_no')
                                <div class="invalid-feedback">{{ $message }}</div>
                            @enderror
                        </div>

                        <!-- Course / Department -->
                        <div class="mb-3">
                            <label class="form-label fw-semibold">Branch / Course</label>
                            <select name="course" class="form-select @error('course') is-invalid @enderror" required>
                                <option value="" disabled selected>Select Branch</option>
                                <option value="Computer Engineering" {{ old('course') == 'Computer Engineering' ? 'selected' : '' }}>Computer Engineering</option>
                                <option value="Information Technology" {{ old('course') == 'Information Technology' ? 'selected' : '' }}>Information Technology</option>
                                <option value="Mechanical Engineering" {{ old('course') == 'Mechanical Engineering' ? 'selected' : '' }}>Mechanical Engineering</option>
                                <option value="Civil Engineering" {{ old('course') == 'Civil Engineering' ? 'selected' : '' }}>Civil Engineering</option>
                            </select>
                            @error('course')
                                <div class="invalid-feedback">{{ $message }}</div>
                            @enderror
                        </div>

                        <!-- Phone Number -->
                        <div class="mb-4">
                            <label class="form-label fw-semibold">Phone Number</label>
                            <input type="tel" name="phone" class="form-control @error('phone') is-invalid @enderror" value="{{ old('phone') }}" placeholder="e.g. 9876543210" required>
                            @error('phone')
                                <div class="invalid-feedback">{{ $message }}</div>
                            @enderror
                        </div>

                        <!-- Action Buttons -->
                        <div class="d-flex justify-content-between align-items-center">
                            <a href="{{ route('students.index') }}" class="btn btn-outline-secondary">
                                <i class="bi bi-arrow-left me-1"></i>View All Students
                            </a>
                            <button type="submit" class="btn btn-primary px-4 fw-semibold">
                                <i class="bi bi-save me-1"></i>Save Student Record
                            </button>
                        </div>
                    </form>

                </div>
            </div>
        </div>
    </div>
</div>
@endsection
