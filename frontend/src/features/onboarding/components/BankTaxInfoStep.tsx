import { TextField, Box } from "@mui/material";
import { type BankTaxInfo } from "../../../types/profile";

interface Props {
  values: BankTaxInfo;
  onChange: (field: keyof BankTaxInfo, value: string) => void;
}

export function BankTaxInfoStep({ values, onChange }: Props) {
  return (
    <Box display="flex" flexDirection="column" gap={2}>
      <TextField
        label="IBAN"
        value={values.iban}
        onChange={(e) => onChange("iban", e.target.value)}
        fullWidth
      />
      <TextField
        label="BIC"
        value={values.bic}
        onChange={(e) => onChange("bic", e.target.value)}
        fullWidth
      />
      <TextField
        label="Tax ID"
        value={values.taxId}
        onChange={(e) => onChange("taxId", e.target.value)}
        fullWidth
      />
      <TextField
        label="VAT Number"
        value={values.vatNumber}
        onChange={(e) => onChange("vatNumber", e.target.value)}
        fullWidth
      />
    </Box>
  );
}
