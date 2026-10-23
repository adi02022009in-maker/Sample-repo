@extends('layouts.app')

@section('title', 'Book Issue & Return Records - Vibe Library')

@section('content')
<div class="container">
    <div class="d-flex flex-column flex-md-row justify-content-between align-items-md-center mb-4 gap-3">
        <div>
            <h2 class="fw-bold mb-1"><i class="bi bi-arrow-left-right text-success me-2"></i>Book Issue & Return Management</h2>
            <p class="text-secondary mb-0">Module 2: Transaction Circulation Tracking</p>
        </div>
        @auth
            <a href="{{ route('borrows.create') }}" class="btn btn-success fw-semibold shadow-sm">
                <i class="bi bi-journal-plus me-1"></i>Issue Book to Member
            </a>
        @endauth
    </div>

    <!-- Borrow Records Table -->
    <div class="card border-0 shadow-sm rounded-3">
        <div class="card-body p-0">
            <div class="table-responsive">
                <table class="table table-hover align-middle mb-0">
                    <thead class="table-light">
                        <tr>
                            <th class="ps-3">ID</th>
                            <th>Member / Student</th>
                            <th>Book Title</th>
                            <th>Issued Date</th>
                            <th>Due Date</th>
                            <th>Return Date</th>
                            <th>Status</th>
                            @auth <th class="text-center">Action</th> @endauth
                        </tr>
                    </thead>
                    <tbody>
                        @forelse($borrows as $borrow)
                            <tr>
                                <td class="ps-3 fw-bold text-muted">#{{ $borrow->id }}</td>
                                <td class="fw-semibold">{{ $borrow->user->name }}</td>
                                <td>{{ $borrow->book->title }}</td>
                                <td>{{ $borrow->borrow_date }}</td>
                                <td>{{ $borrow->due_date }}</td>
                                <td>{{ $borrow->return_date ?? '—' }}</td>
                                <td>
                                    @if($borrow->status === 'Issued')
                                        <span class="badge bg-warning text-dark"><i class="bi bi-clock me-1"></i>Issued</span>
                                    @else
                                        <span class="badge bg-success"><i class="bi bi-check2-circle me-1"></i>Returned</span>
                                    @endif
                                </td>
                                @auth
                                    <td class="text-center">
                                        @if($borrow->status === 'Issued')
                                            <form action="{{ route('borrows.return', $borrow->id) }}" method="POST" class="d-inline">
                                                @csrf
                                                <button type="submit" class="btn btn-sm btn-outline-success fw-semibold">
                                                    <i class="bi bi-box-arrow-in-down me-1"></i>Mark Return
                                                </button>
                                            </form>
                                        @else
                                            <span class="text-muted small">Completed</span>
                                        @endif
                                    </td>
                                @endauth
                            </tr>
                        @empty
                            <tr>
                                <td colspan="8" class="text-center py-4 text-muted">No circulation records found.</td>
                            </tr>
                        @endforelse
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
@endsection
