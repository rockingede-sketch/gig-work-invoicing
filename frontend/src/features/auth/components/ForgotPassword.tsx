import { type SubmitEvent, useState } from "react";
import {
  Box,
  Button,
  Card,
  CardContent,
  TextField,
  Typography,
  Link,
} from "@mui/material";
import { Link as RouterLink } from "react-router-dom";

export default function ForgotPassword() {
  const [email, setEmail] = useState("");

  const handleSubmit = (e: SubmitEvent<HTMLFormElement>) => {
    e.preventDefault();
    console.log("Password reset request for:", email);
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
        sx={{
          width: "100%",
          maxWidth: 420,
          boxShadow: 3,
          borderRadius: 2,
        }}
      >
        <CardContent sx={{ p: 4 }}>
          <Typography variant="h5" fontWeight={600} mb={2}>
            Unohditko salasanasi
          </Typography>

          <Typography variant="body2" color="text.secondary" mb={3}>
            Anna sähköpostiosoitteesi, niin lähetämme ohjeet salasanan palauttamiseksi.
          </Typography>

          <form onSubmit={handleSubmit}>
            <Box sx={{ display: "grid", gap: 16 }}>
              <TextField
                label="Sähköposti"
                type="email"
                fullWidth
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />

              <Button type="submit" variant="contained" size="large" sx={{ py: 1.2 }}>
                Lähetä palautuslinkki
              </Button>
            </Box>
          </form>

          <Typography variant="body2" color="text.secondary" textAlign="center" mt={3}>
            Muistitko salasanasi? {" "}
            <Link component={RouterLink} to="/login" underline="hover">
              Kirjaudu sisään
            </Link>
          </Typography>
        </CardContent>
      </Card>
    </Box>
  );
}
