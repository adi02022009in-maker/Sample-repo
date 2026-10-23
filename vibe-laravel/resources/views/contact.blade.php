@extends('layouts.app')

@section('title', 'Contact Us - Vibe Coding Portal')

@section('content')
<div class="container">
    <div class="row justify-content-center">
        <div class="col-lg-6">
            <div class="card border-0 shadow-sm p-4">
                <h3 class="fw-bold mb-3">Contact Information</h3>
                <p class="text-secondary mb-4">Have questions regarding DI05000121 practical submissions? Get in touch below.</p>
                
                <form onsubmit="event.preventDefault(); alert('Message sent successfully!');">
                    <div class="mb-3">
                        <label class="form-label fw-semibold">Your Name</label>
                        <input type="text" class="form-control" placeholder="Enter your name" required>
                    </div>
                    <div class="mb-3">
                        <label class="form-label fw-semibold">Enrollment Number</label>
                        <input type="text" class="form-control" placeholder="e.g. 246250307086" required>
                    </div>
                    <div class="mb-3">
                        <label class="form-label fw-semibold">Message / Query</label>
                        <textarea class="form-control" rows="3" placeholder="Enter your query here..."></textarea>
                    </div>
                    <button type="submit" class="btn btn-primary w-100 fw-semibold">Submit Inquiry</button>
                </form>
            </div>
        </div>
    </div>
</div>
@endsection
