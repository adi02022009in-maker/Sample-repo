@extends('layouts.app')

@section('title', 'Issue Book - Vibe Library')

@section('content')
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-7">
            <div class="card border-0 shadow-sm rounded-3">
                <div class="card-header bg-success text-white py-3">
                    <h5 class="mb-0 fw-bold"><i class="bi bi-journal-plus me-2"></i>Issue Book to Member</h5>
                </div>
                <div class="card-body p-4">
                    @if ($errors->any())
                        <div class="alert alert-danger mb-3">
                            <ul class="mb-0">
                                @foreach ($errors->all() as $error) <li>{{ $error }}</li> @endforeach
                            </ul>
                        </div>
                    @endif

                    <form action="{{ route('borrows.store') }}" method="POST">
                        @csrf
                        <div class="mb-3">
                            <label class="form-label fw-semibold">Select Member / User</label>
                            <select name="user_id" class="form-select" required>
                                @foreach($users as $user)
                                    <option value="{{ $user->id }}">{{ $user->name }} ({{ $user->email }})</option>
                                @endforeach
                            </select>
                        </div>
                        <div class="mb-3">
                            <label class="form-label fw-semibold">Select Available Book</label>
                            <select name="book_id" class="form-select" required>
                                @foreach($books as $book)
                                    <option value="{{ $book->id }}">{{ $book->title }} (Available: {{ $book->available_copies }})</option>
                                @endforeach
                            </select>
                        </div>
                        <div class="row mb-3">
                            <div class="col">
                                <label class="form-label fw-semibold">Issue Date</label>
                                <input type="date" name="borrow_date" class="form-control" value="{{ date('Y-m-d') }}" required>
                            </div>
                            <div class="col">
                                <label class="form-label fw-semibold">Due Date</label>
                                <input type="date" name="due_date" class="form-control" value="{{ date('Y-m-d', strtotime('+14 days')) }}" required>
                            </div>
                        </div>
                        <div class="d-flex justify-content-between">
                            <a href="{{ route('borrows.index') }}" class="btn btn-outline-secondary">Cancel</a>
                            <button type="submit" class="btn btn-success px-4 fw-bold">Confirm Issue</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
@endsection
