import { type SubmitEvent, useState } from "react";
import {
  Box,
  Button,
  Card,
  CardContent,
  TextField,
  Typography,
  Stack,
  Link,
} from "@mui/material";

export default function CreateAccount() {
  const [form, setForm] = useState({
    email: "",
    password: "",
    confirmPassword: "",
    firstName: "",
    lastName: "",
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e: SubmitEvent<HTMLFormElement>) => {
    e.preventDefault();
    console.log("Create account:", form);
  };

  return (
    <Box
      sx={{
        minHeight: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        backgroundColor: "#f5f5f5",
        px: 2,
      }}
    >
      <Card
        sx={{ width: "100%", maxWidth: 420, borderRadius: 3, boxShadow: 3 }}
      >
        <CardContent sx={{ p: 4 }}>
          <Typography variant="h5" fontWeight={600} textAlign="center" mb={2}>
            Luo tili
          </Typography>

          <Typography
            variant="body2"
            color="text.secondary"
            textAlign="center"
            mb={3}
          >
            Aloita palvelun käyttö luomalla tilisi
          </Typography>

          <form onSubmit={handleSubmit}>
            <Stack spacing={2}>
              <TextField
                label="Etunimi"
                name="firstName"
                fullWidth
                value={form.firstName}
                onChange={handleChange}
              />

              <TextField
                label="Sukunimi"
                name="lastName"
                fullWidth
                value={form.lastName}
                onChange={handleChange}
              />

              <TextField
                label="Sähköposti"
                name="email"
                type="email"
                fullWidth
                value={form.email}
                onChange={handleChange}
              />

              <TextField
                label="Salasana"
                name="password"
                type="password"
                fullWidth
                value={form.password}
                onChange={handleChange}
              />

              <TextField
                label="Vahvista salasana"
                name="confirmPassword"
                type="password"
                fullWidth
                value={form.confirmPassword}
                onChange={handleChange}
              />

              <Button
                type="submit"
                variant="contained"
                size="large"
                sx={{ mt: 1, borderRadius: 2 }}
              >
                Luo tili
              </Button>
            </Stack>
          </form>

          <Typography
            variant="body2"
            textAlign="center"
            mt={3}
            color="text.secondary"
          >
            Onko sinulla jo tili?{" "}
            <Link href="/login" underline="hover">
              Kirjaudu sisään
            </Link>
          </Typography>
        </CardContent>
      </Card>
    </Box>
  );
}
