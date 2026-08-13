import type { User } from "../types/user";
import RoleBadge from "./RoleBadge";

interface UsersTableProps {
  users: User[];
}

export default function UsersTable({ users }: UsersTableProps) {
  return (
    <table className="users-table">
      <thead>
        <tr>
          <th>Name</th>
          <th>Email</th>
          <th>Role</th>
          <th>Department</th>
          <th>Phone</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        {users.map((user) => (
          <tr key={user._id}>
            <td>{user.full_name}</td>
            <td>{user.email}</td>
            <td>
              <RoleBadge role={user.role} />
            </td>
            <td>{user.department}</td>
            <td>{user.phone}</td>
            <td>{user.is_active ? "Active" : "Inactive"}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
