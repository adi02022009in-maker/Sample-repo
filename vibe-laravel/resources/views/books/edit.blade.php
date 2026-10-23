@extends('layouts.app')

@section('title', 'Edit Book - Vibe Library')

@section('content')
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-7">
            <div class="card border-0 shadow-sm rounded-3">
                <div class="card-header bg-warning text-dark py-3">
                    <h5 class="mb-0 fw-bold"><i class="bi bi-pencil-square me-2"></i>Edit Book Details</h5>
                </div>
                <div class="card-body p-4">
                    <form action="{{ route('books.update', $book->id) }}" method="POST">
                        @csrf
                        @method('PUT')
                        <div class="mb-3">
                            <label class="form-label fw-semibold">Book Title</label>
                            <input type="text" name="title" class="form-control" value="{{ old('title', $book->title) }}" required>
                        </div>
                        <div class="mb-3">
                            <label class="form-label fw-semibold">Author</label>
                            <input type="text" name="author" class="form-control" value="{{ old('author', $book->author) }}" required>
                        </div>
                        <div class="mb-3">
                            <label class="form-label fw-semibold">ISBN</label>
                            <input type="text" name="isbn" class="form-control" value="{{ old('isbn', $book->isbn) }}" required>
                        </div>
                        <div class="mb-3">
                            <label class="form-label fw-semibold">Category</label>
                            <input type="text" name="category" class="form-control" value="{{ old('category', $book->category) }}" required>
                        </div>
                        <div class="row mb-3">
                            <div class="col">
                                <label class="form-label fw-semibold">Total Copies</label>
                                <input type="number" name="total_copies" class="form-control" value="{{ old('total_copies', $book->total_copies) }}" min="1" required>
                            </div>
                            <div class="col">
                                <label class="form-label fw-semibold">Available Copies</label>
                                <input type="number" name="available_copies" class="form-control" value="{{ old('available_copies', $book->available_copies) }}" min="0" required>
                            </div>
                        </div>
                        <div class="d-flex justify-content-between">
                            <a href="{{ route('books.index') }}" class="btn btn-outline-secondary">Cancel</a>
                            <button type="submit" class="btn btn-warning px-4 fw-bold">Update Book</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
@endsection
