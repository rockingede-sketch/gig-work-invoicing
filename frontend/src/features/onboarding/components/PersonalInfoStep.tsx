import { TextField, Box } from "@mui/material";
import { type PersonalInfo } from "../../../types/profile";

interface Props {
  values: PersonalInfo;
  onChange: (field: keyof PersonalInfo, value: string) => void;
}

export function PersonalInfoStep({ values, onChange }: Props) {
  return (
    <Box display="flex" flexDirection="column" gap={2}>
      <TextField
        label="First Name"
        value={values.firstName}
        onChange={(e) => onChange("firstName", e.target.value)}
        fullWidth
      />
      <TextField
        label="Last Name"
        value={values.lastName}
        onChange={(e) => onChange("lastName", e.target.value)}
        fullWidth
      />
      <TextField
        label="Email"
        type="email"
        value={values.email}
        onChange={(e) => onChange("email", e.target.value)}
        fullWidth
      />
    </Box>
  );
}
