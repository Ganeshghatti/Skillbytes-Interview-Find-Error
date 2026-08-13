import type { StaffRole } from "../types/user";

const LABELS: Record<StaffRole, string> = {
  admin: "Admin",
  manager: "Manager",
  teacher: "Teacher",
};

export default function RoleBadge({ role }: { role: StaffRole }) {
  return <span className={`role-badge role-badge--${role}`}>{LABELS[role]}</span>;
}
