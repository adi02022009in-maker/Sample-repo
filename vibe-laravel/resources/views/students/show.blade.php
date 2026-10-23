@extends('layouts.app')

@section('title', 'Student Profile - ' . $student->name)

@section('content')
<div class="container">
    <div class="row justify-content-center">
        <div class="col-lg-6">
            <div class="card border-0 shadow-sm rounded-3">
                <div class="card-header bg-primary text-white py-3 d-flex justify-content-between align-items-center">
                    <h5 class="mb-0 fw-bold">
                        <i class="bi bi-person-badge-fill me-2"></i>Student Details
                    </h5>
                    <span class="badge bg-light text-primary fw-bold">ID: #{{ $student->id }}</span>
                </div>
                <div class="card-body p-4">
                    <div class="text-center mb-4">
                        <div class="display-4 text-primary mb-2">
                            <i class="bi bi-person-circle"></i>
                        </div>
                        <h4 class="fw-bold mb-1">{{ $student->name }}</h4>
                        <span class="badge bg-primary-subtle text-primary border px-3 py-2">
                            {{ $student->course }}
                        </span>
                    </div>

                    <ul class="list-group list-group-flush mb-4">
                        <li class="list-group-item d-flex justify-content-between align-items-center py-3">
                            <span class="text-muted"><i class="bi bi-card-text me-2"></i>Enrollment Number</span>
                            <span class="fw-semibold">{{ $student->enrollment_no }}</span>
                        </li>
                        <li class="list-group-item d-flex justify-content-between align-items-center py-3">
                            <span class="text-muted"><i class="bi bi-envelope me-2"></i>Email Address</span>
                            <span class="fw-semibold">{{ $student->email }}</span>
                        </li>
                        <li class="list-group-item d-flex justify-content-between align-items-center py-3">
                            <span class="text-muted"><i class="bi bi-telephone me-2"></i>Phone Number</span>
                            <span class="fw-semibold">{{ $student->phone }}</span>
                        </li>
                        <li class="list-group-item d-flex justify-content-between align-items-center py-3">
                            <span class="text-muted"><i class="bi bi-calendar-check me-2"></i>Registration Date</span>
                            <span class="text-secondary small">{{ $student->created_at->format('d M Y, h:i A') }}</span>
                        </li>
                    </ul>

                    <div class="d-flex justify-content-between">
                        <a href="{{ route('students.index') }}" class="btn btn-outline-secondary">
                            <i class="bi bi-arrow-left me-1"></i>Back to Records List
                        </a>
                        <a href="{{ route('students.edit', $student->id) }}" class="btn btn-warning fw-semibold">
                            <i class="bi bi-pencil-square me-1"></i>Edit Record
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
@endsection
