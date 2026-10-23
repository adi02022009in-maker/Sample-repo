@extends('layouts.app')

@section('title', 'Add New Book - Vibe Library')

@section('content')
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-7">
            <div class="card border-0 shadow-sm rounded-3">
                <div class="card-header bg-primary text-white py-3">
                    <h5 class="mb-0 fw-bold"><i class="bi bi-plus-circle me-2"></i>Add Book to Inventory</h5>
                </div>
                <div class="card-body p-4">
                    @if ($errors->any())
                        <div class="alert alert-danger mb-3">
                            <ul class="mb-0">
                                @foreach ($errors->all() as $error) <li>{{ $error }}</li> @endforeach
                            </ul>
                        </div>
                    @endif

                    <form action="{{ route('books.store') }}" method="POST">
                        @csrf
                        <div class="mb-3">
                            <label class="form-label fw-semibold">Book Title</label>
                            <input type="text" name="title" class="form-control" placeholder="e.g. Computer Networks" required>
                        </div>
                        <div class="mb-3">
                            <label class="form-label fw-semibold">Author</label>
                            <input type="text" name="author" class="form-control" placeholder="e.g. Andrew S. Tanenbaum" required>
                        </div>
                        <div class="mb-3">
                            <label class="form-label fw-semibold">ISBN</label>
                            <input type="text" name="isbn" class="form-control" placeholder="e.g. 978-0132126953" required>
                        </div>
                        <div class="mb-3">
                            <label class="form-label fw-semibold">Category</label>
                            <input type="text" name="category" class="form-control" placeholder="e.g. Networking" required>
                        </div>
                        <div class="mb-3">
                            <label class="form-label fw-semibold">Total Copies</label>
                            <input type="number" name="total_copies" class="form-control" min="1" value="5" required>
                        </div>
                        <div class="d-flex justify-content-between">
                            <a href="{{ route('books.index') }}" class="btn btn-outline-secondary">Cancel</a>
                            <button type="submit" class="btn btn-primary px-4 fw-bold">Save Book</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
@endsection
