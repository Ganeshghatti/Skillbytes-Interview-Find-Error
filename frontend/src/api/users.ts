import type { PaginatedUsersResponse } from "../types/user";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000";

export async function fetchUsers(page: number, limit: number): Promise<PaginatedUsersResponse> {
  const url = `${API_BASE_URL}/api/users?page=${page}&limit=${limit}`;
  const response = await fetch(url);

  if (!response.ok) {
    throw new Error(`Request failed with status ${response.status}`);
  }

  return response.json();
}
