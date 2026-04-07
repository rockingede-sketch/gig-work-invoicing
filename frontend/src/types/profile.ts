export interface PersonalInfo {
  firstName: string;
  lastName: string;
  email: string;
}

export interface BankTaxInfo {
  iban: string;
  bic: string;
  taxId: string;
  vatNumber: string;
}

export interface ProfileData extends PersonalInfo, BankTaxInfo {}
