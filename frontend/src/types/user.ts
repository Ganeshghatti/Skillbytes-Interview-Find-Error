export type StaffRole = "manager" | "teacher" | "admin";

export interface User {
  _id: string;
  full_name: string;
  email: string;
  role: StaffRole;
  department: string;
  phone: string;
  is_active: boolean;
  created_at: string;
}

export interface PaginatedUsersResponse {
  items: User[];
  total: number;
  page: number;
  limit: number;
  total_pages: number;
}
