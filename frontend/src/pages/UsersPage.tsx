import { useEffect, useState } from "react";
import { fetchUsers } from "../api/users";
import type { User } from "../types/user";
import UsersTable from "../components/UsersTable";
import Pagination from "../components/Pagination";

const PAGE_SIZE = 20;

export default function UsersPage() {
  const [users, setUsers] = useState<User[]>([]);
  const [page, setPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;

    setIsLoading(true);
    setError(null);

    fetchUsers(page, PAGE_SIZE)
      .then((data) => {
        if (cancelled) return;
        setUsers(data.items);
        setTotalPages(data.total_pages);
      })
      .catch((err: Error) => {
        if (cancelled) return;
        setError(err.message);
      })
      .finally(() => {
        if (cancelled) return;
        setIsLoading(false);
      });

    return () => {
      cancelled = true;
    };
  }, [page]);

  return (
    <section className="users-page">
      <div className="users-page__header">
        <h1>Users</h1>
        <p className="users-page__subtitle">Manager, teacher, and admin accounts</p>
      </div>

      {isLoading && <div className="state-banner state-banner--loading">Loading users...</div>}

      {error && (
        <div className="state-banner state-banner--error">
          Failed to load users: {error}
        </div>
      )}

      {!isLoading && !error && (
        <>
          <UsersTable users={users} />
          <Pagination page={page} totalPages={totalPages} onPageChange={setPage} />
        </>
      )}
    </section>
  );
}
