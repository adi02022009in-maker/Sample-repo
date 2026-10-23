<?php

namespace App\Http\Controllers;

use App\Models\Book;
use App\Models\Borrow;
use App\Models\User;
use Illuminate\Http\Request;

class BorrowController extends Controller
{
    public function index()
    {
        $borrows = Borrow::with(['user', 'book'])->orderBy('id', 'desc')->get();
        return view('borrows.index', compact('borrows'));
    }

    public function create()
    {
        $users = User::all();
        $books = Book::where('available_copies', '>', 0)->get();
        return view('borrows.create', compact('users', 'books'));
    }

    public function store(Request $request)
    {
        $validated = $request->validate([
            'user_id' => 'required|exists:users,id',
            'book_id' => 'required|exists:books,id',
            'borrow_date' => 'required|date',
            'due_date' => 'required|date|after_or_equal:borrow_date',
        ]);

        $book = Book::findOrFail($validated['book_id']);

        if ($book->available_copies < 1) {
            return back()->withErrors(['book_id' => 'No copies of this book are currently available.']);
        }

        Borrow::create([
            'user_id' => $validated['user_id'],
            'book_id' => $validated['book_id'],
            'borrow_date' => $validated['borrow_date'],
            'due_date' => $validated['due_date'],
            'status' => 'Issued',
        ]);

        $book->decrement('available_copies');

        return redirect()->route('borrows.index')->with('success', 'Book issued successfully!');
    }

    public function returnBook(Borrow $borrow)
    {
        if ($borrow->status === 'Returned') {
            return back()->with('info', 'Book is already marked as returned.');
        }

        $borrow->update([
            'return_date' => now()->toDateString(),
            'status' => 'Returned',
        ]);

        $borrow->book->increment('available_copies');

        return redirect()->route('borrows.index')->with('success', 'Book returned and stock restored!');
    }

    public function summaryReport()
    {
        $totalBooks = Book::sum('total_copies');
        $availableBooks = Book::sum('available_copies');
        $issuedBooks = Borrow::where('status', 'Issued')->count();
        $returnedBooks = Borrow::where('status', 'Returned')->count();
        $recentBorrows = Borrow::with(['user', 'book'])->latest()->take(5)->get();

        return view('reports.summary', compact(
            'totalBooks',
            'availableBooks',
            'issuedBooks',
            'returnedBooks',
            'recentBorrows'
        ));
    }
}
