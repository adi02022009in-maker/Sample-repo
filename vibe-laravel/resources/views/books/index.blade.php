@extends('layouts.app')

@section('title', 'Library Books Directory - Vibe Library')

@section('content')
<div class="container">
    <div class="d-flex flex-column flex-md-row justify-content-between align-items-md-center mb-4 gap-3">
        <div>
            <h2 class="fw-bold mb-1"><i class="bi bi-book-half text-primary me-2"></i>Library Books Inventory</h2>
            <p class="text-secondary mb-0">Module 1: Book Inventory CRUD & Search Filter</p>
        </div>
        @auth
            <a href="{{ route('books.create') }}" class="btn btn-primary fw-semibold shadow-sm">
                <i class="bi bi-plus-circle me-1"></i>Add New Book
            </a>
        @endauth
    </div>

    <!-- Search and Filter Bar -->
    <div class="card border-0 shadow-sm p-3 mb-4 bg-white">
        <form method="GET" action="{{ route('books.index') }}" class="row g-2 align-items-center">
            <div class="col-md-6">
                <div class="input-group">
                    <span class="input-group-text bg-light"><i class="bi bi-search"></i></span>
                    <input type="text" name="search" class="form-control" placeholder="Search by title, author, or ISBN..." value="{{ request('search') }}">
                </div>
            </div>
            <div class="col-md-4">
                <select name="category" class="form-select">
                    <option value="">All Categories</option>
                    @foreach($categories as $cat)
                        <option value="{{ $cat }}" {{ request('category') == $cat ? 'selected' : '' }}>{{ $cat }}</option>
                    @endforeach
                </select>
            </div>
            <div class="col-md-2 d-flex gap-2">
                <button type="submit" class="btn btn-primary w-100 fw-semibold">Filter</button>
                <a href="{{ route('books.index') }}" class="btn btn-outline-secondary">Reset</a>
            </div>
        </form>
    </div>

    <!-- Books Table -->
    <div class="card border-0 shadow-sm rounded-3">
        <div class="card-body p-0">
            <div class="table-responsive">
                <table class="table table-hover align-middle mb-0">
                    <thead class="table-light">
                        <tr>
                            <th class="ps-3">ID</th>
                            <th>Book Title</th>
                            <th>Author</th>
                            <th>ISBN</th>
                            <th>Category</th>
                            <th>Total Copies</th>
                            <th>Available</th>
                            @auth <th class="text-center">Actions</th> @endauth
                        </tr>
                    </thead>
                    <tbody>
                        @forelse($books as $book)
                            <tr>
                                <td class="ps-3 fw-bold text-muted">#{{ $book->id }}</td>
                                <td class="fw-semibold text-dark">{{ $book->title }}</td>
                                <td>{{ $book->author }}</td>
                                <td><span class="badge bg-secondary-subtle text-secondary font-monospace">{{ $book->isbn }}</span></td>
                                <td><span class="badge bg-info-subtle text-info border">{{ $book->category }}</span></td>
                                <td>{{ $book->total_copies }}</td>
                                <td>
                                    @if($book->available_copies > 0)
                                        <span class="badge bg-success">{{ $book->available_copies }} In Stock</span>
                                    @else
                                        <span class="badge bg-danger">Out of Stock</span>
                                    @endif
                                </td>
                                @auth
                                    <td class="text-center">
                                        <div class="btn-group btn-group-sm">
                                            <a href="{{ route('books.edit', $book->id) }}" class="btn btn-outline-warning" title="Edit">
                                                <i class="bi bi-pencil-square"></i>
                                            </a>
                                            <form action="{{ route('books.destroy', $book->id) }}" method="POST" onsubmit="return confirm('Delete this book?');" class="d-inline">
                                                @csrf
                                                @method('DELETE')
                                                <button type="submit" class="btn btn-outline-danger" title="Delete">
                                                    <i class="bi bi-trash"></i>
                                                </button>
                                            </form>
                                        </div>
                                    </td>
                                @endauth
                            </tr>
                        @empty
                            <tr>
                                <td colspan="8" class="text-center py-4 text-muted">No books matched your filter criteria.</td>
                            </tr>
                        @endforelse
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
@endsection
