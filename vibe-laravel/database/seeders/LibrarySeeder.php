<?php

namespace Database\Seeders;

use App\Models\Book;
use App\Models\Borrow;
use App\Models\User;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\Hash;

class LibrarySeeder extends Seeder
{
    public function run(): void
    {
        $user = User::firstOrCreate(
            ['email' => 'admin@library.com'],
            [
                'name' => 'Librarian Admin',
                'password' => Hash::make('password123'),
            ]
        );

        $book1 = Book::firstOrCreate(
            ['isbn' => '978-1118063330'],
            [
                'title' => 'Operating System Concepts',
                'author' => 'Silberschatz',
                'category' => 'Computer Science',
                'total_copies' => 5,
                'available_copies' => 4,
            ]
        );

        $book2 = Book::firstOrCreate(
            ['isbn' => '978-0073523323'],
            [
                'title' => 'Database System Concepts',
                'author' => 'Silberschatz & Korth',
                'category' => 'Database Systems',
                'total_copies' => 4,
                'available_copies' => 4,
            ]
        );

        $book3 = Book::firstOrCreate(
            ['isbn' => '978-0132350884'],
            [
                'title' => 'Clean Code',
                'author' => 'Robert C. Martin',
                'category' => 'Software Engineering',
                'total_copies' => 3,
                'available_copies' => 3,
            ]
        );

        if (Borrow::count() === 0) {
            Borrow::create([
                'user_id' => $user->id,
                'book_id' => $book1->id,
                'borrow_date' => now()->toDateString(),
                'due_date' => now()->addDays(14)->toDateString(),
                'status' => 'Issued',
            ]);
        }
    }
}
