import { Typography, Button, Box, Grid, Container } from "@mui/material";
import { Link } from "react-router-dom";

export default function Homepage() {
  return (
    <Box sx={{ flexGrow: 1 }}>
      {/* HOMEPAGE CONTENT */}
      <Container sx={{ mt: 6 }}>
        <Grid container spacing={4}>
          <Grid xs={12} md={6}>
            <Typography variant="h3" fontWeight={700} gutterBottom>
              Tervetuloa Keikkalaskuun
            </Typography>

            <Typography variant="body1" sx={{ mb: 3 }}>
              Helppo ja nopea tapa laskuttaa ilman omaa yritystä. Aloita
              laskutus muutamassa minuutissa.
            </Typography>

            <Button
              variant="contained"
              size="large"
              component={Link}
              to="/login"
            >
              Aloita nyt
            </Button>
          </Grid>

          <Grid xs={12} md={6}>
            <Box
              sx={{
                width: "100%",
                height: 300,
                bgcolor: "grey.200",
                borderRadius: 2,
              }}
            />
          </Grid>
        </Grid>

        {/* FEATURES SECTION */}
        <Grid container spacing={4} sx={{ mt: 8 }}>
          <Grid xs={12} md={4}>
            <Box sx={{ p: 3, bgcolor: "grey.100", borderRadius: 2 }}>
              <Typography variant="h6" fontWeight={600}>
                Nopea laskutus
              </Typography>
              <Typography variant="body2">
                Luo lasku muutamassa minuutissa ja lähetä se asiakkaalle.
              </Typography>
            </Box>
          </Grid>

          <Grid xs={12} md={4}>
            <Box sx={{ p: 3, bgcolor: "grey.100", borderRadius: 2 }}>
              <Typography variant="h6" fontWeight={600}>
                Ei paperisotaa
              </Typography>
              <Typography variant="body2">
                Hoidamme verot, vakuutukset ja muut velvoitteet puolestasi.
              </Typography>
            </Box>
          </Grid>

          <Grid xs={12} md={4}>
            <Box sx={{ p: 3, bgcolor: "grey.100", borderRadius: 2 }}>
              <Typography variant="h6" fontWeight={600}>
                Turvallinen palvelu
              </Typography>
              <Typography variant="body2">
                Luotettava suomalainen laskutuspalvelu.
              </Typography>
            </Box>
          </Grid>
        </Grid>
      </Container>
    </Box>
  );
}
