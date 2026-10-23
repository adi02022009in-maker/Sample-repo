@extends('layouts.app')

@section('title', 'Registered Students List - Vibe Coding')

@section('content')
<div class="container">
    <div class="d-flex flex-column flex-md-row justify-content-between align-items-md-center mb-4 gap-3">
        <div>
            <div class="d-flex align-items-center gap-2">
                <h2 class="fw-bold mb-0">Student Records Directory</h2>
                <span class="badge bg-primary rounded-pill fs-6">{{ $students->count() }} Total</span>
            </div>
            <p class="text-secondary mb-0">Live records retrieved from SQLite database using Eloquent ORM</p>
        </div>
        <a href="{{ route('students.create') }}" class="btn btn-primary fw-semibold shadow-sm">
            <i class="bi bi-person-plus-fill me-1"></i>Register New Student
        </a>
    </div>

    <!-- Success Message Alert -->
    @if(session('success'))
        <div class="alert alert-success alert-dismissible fade show shadow-sm" role="alert">
            <i class="bi bi-check-circle-fill me-2"></i>{{ session('success') }}
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
    @endif

    <div class="card border-0 shadow-sm rounded-3">
        <div class="card-body p-0">
            <div class="table-responsive">
                <table class="table table-hover align-middle mb-0">
                    <thead class="table-light">
                        <tr>
                            <th class="ps-3">ID</th>
                            <th>Full Name</th>
                            <th>Enrollment No.</th>
                            <th>Branch / Department</th>
                            <th>Email Address</th>
                            <th>Phone</th>
                            <th class="text-center">Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        @forelse ($students as $student)
                            <tr>
                                <td class="ps-3 fw-bold text-muted">#{{ $student->id }}</td>
                                <td class="fw-semibold text-dark">
                                    <i class="bi bi-person-fill text-primary me-1"></i>{{ $student->name }}
                                </td>
                                <td>
                                    <span class="badge bg-secondary-subtle text-secondary border font-monospace">
                                        {{ $student->enrollment_no }}
                                    </span>
                                </td>
                                <td>
                                    <span class="badge bg-primary-subtle text-primary border">
                                        {{ $student->course }}
                                    </span>
                                </td>
                                <td>
                                    <a href="mailto:{{ $student->email }}" class="text-decoration-none text-muted">
                                        {{ $student->email }}
                                    </a>
                                </td>
                                <td class="text-secondary">{{ $student->phone }}</td>
                                <td class="text-center">
                                    <div class="btn-group btn-group-sm">
                                        <a href="{{ route('students.show', $student->id) }}" class="btn btn-outline-info" title="View Profile">
                                            <i class="bi bi-eye"></i>
                                        </a>
                                        <a href="{{ route('students.edit', $student->id) }}" class="btn btn-outline-primary" title="Edit Record">
                                            <i class="bi bi-pencil-square"></i>
                                        </a>
                                        <form action="{{ route('students.destroy', $student->id) }}" method="POST" onsubmit="return confirm('Are you sure you want to delete this record?');" class="d-inline">
                                            @csrf
                                            @method('DELETE')
                                            <button type="submit" class="btn btn-outline-danger" title="Delete Record">
                                                <i class="bi bi-trash"></i>
                                            </button>
                                        </form>
                                    </div>
                                </td>
                            </tr>
                        @empty
                            <tr>
                                <td colspan="7" class="text-center py-5 text-muted">
                                    <i class="bi bi-inbox" style="font-size: 2.5rem;"></i>
                                    <p class="mt-2 mb-2">No student records found in the database.</p>
                                    <a href="{{ route('students.create') }}" class="btn btn-sm btn-outline-primary">Register the first student</a>
                                </td>
                            </tr>
                        @endforelse
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
@endsection
