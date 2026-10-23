@extends('layouts.app')

@section('title', 'Library Analytics & Summary Report - Vibe Library')

@section('content')
<div class="container">
    <div class="mb-4">
        <h2 class="fw-bold mb-1"><i class="bi bi-graph-up-arrow text-primary me-2"></i>Library Operations Summary Report</h2>
        <p class="text-secondary mb-0">System performance metrics and circulation analytics</p>
    </div>

    <!-- Summary KPI Cards -->
    <div class="row g-3 mb-4">
        <div class="col-md-3">
            <div class="card border-0 shadow-sm p-3 border-start border-4 border-primary">
                <span class="text-muted small fw-bold">TOTAL BOOK STOCK</span>
                <h3 class="fw-bold mt-1 text-primary">{{ $totalBooks }}</h3>
            </div>
        </div>
        <div class="col-md-3">
            <div class="card border-0 shadow-sm p-3 border-start border-4 border-success">
                <span class="text-muted small fw-bold">AVAILABLE IN SHELF</span>
                <h3 class="fw-bold mt-1 text-success">{{ $availableBooks }}</h3>
            </div>
        </div>
        <div class="col-md-3">
            <div class="card border-0 shadow-sm p-3 border-start border-4 border-warning">
                <span class="text-muted small fw-bold">CURRENTLY ISSUED</span>
                <h3 class="fw-bold mt-1 text-warning">{{ $issuedBooks }}</h3>
            </div>
        </div>
        <div class="col-md-3">
            <div class="card border-0 shadow-sm p-3 border-start border-4 border-info">
                <span class="text-muted small fw-bold">TOTAL RETURNED</span>
                <h3 class="fw-bold mt-1 text-info">{{ $returnedBooks }}</h3>
            </div>
        </div>
    </div>

    <!-- Recent Transactions Table -->
    <div class="card border-0 shadow-sm rounded-3">
        <div class="card-header bg-white py-3">
            <h5 class="fw-bold mb-0">Recent Circulation Activity</h5>
        </div>
        <div class="card-body p-0">
            <div class="table-responsive">
                <table class="table table-hover align-middle mb-0">
                    <thead class="table-light">
                        <tr>
                            <th class="ps-3">ID</th>
                            <th>Member</th>
                            <th>Book</th>
                            <th>Borrow Date</th>
                            <th>Due Date</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        @forelse($recentBorrows as $b)
                            <tr>
                                <td class="ps-3 fw-bold text-muted">#{{ $b->id }}</td>
                                <td>{{ $b->user->name }}</td>
                                <td>{{ $b->book->title }}</td>
                                <td>{{ $b->borrow_date }}</td>
                                <td>{{ $b->due_date }}</td>
                                <td>
                                    <span class="badge {{ $b->status === 'Issued' ? 'bg-warning text-dark' : 'bg-success' }}">
                                        {{ $b->status }}
                                    </span>
                                </td>
                            </tr>
                        @empty
                            <tr><td colspan="6" class="text-center py-3">No activity recorded.</td></tr>
                        @endforelse
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
@endsection
