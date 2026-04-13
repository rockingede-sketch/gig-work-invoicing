PRAGMA foreign_keys = ON;

-- =========================================================
-- Standalone SQLite dumy data seed script based on the uploaded Django models. BACKUP YOUR DJANGO Table or find a restore in the database folder initial data.
--
-- To import this dummy data use for example or use HeidiSQL: 
-- uv run python sqlite3 db.sqlite3 < dummy-data.sql
-- Nick 10.4.2026
-- =========================================================


PRAGMA foreign_keys = ON;
BEGIN TRANSACTION;

INSERT INTO auth_user (
    id, password, last_login, is_superuser, username, last_name,
    email, is_staff, is_active, date_joined, first_name
) VALUES
(101, 'pbkdf2_sha256$600000$dummy$hash001', NULL, 0, 'matti.meikalainen@example.fi', 'Meikäläinen', 'matti.meikalainen@example.fi', 0, 1, '2025-01-05 09:15:00', 'Matti'),
(102, 'pbkdf2_sha256$600000$dummy$hash002', NULL, 0, 'liisa.korhonen@example.fi', 'Korhonen', 'liisa.korhonen@example.fi', 0, 1, '2025-01-06 10:00:00', 'Liisa'),
(103, 'pbkdf2_sha256$600000$dummy$hash003', NULL, 0, 'pekka.virtanen@example.fi', 'Virtanen', 'pekka.virtanen@example.fi', 0, 1, '2025-01-10 08:45:00', 'Pekka'),
(104, 'pbkdf2_sha256$600000$dummy$hash004', NULL, 0, 'sari.lahtinen@example.fi', 'Lahtinen', 'sari.lahtinen@example.fi', 0, 1, '2025-01-12 11:30:00', 'Sari');

-- =========================================================
-- gbsapp_userprofile
-- =========================================================
INSERT INTO gbsapp_userprofile (
    id, user_id, confirmed, valid_from, valid_to
) VALUES
(101, 101, 1, '2025-01-05', NULL),
(102, 102, 1, '2025-01-06', NULL),
(103, 103, 1, '2025-01-10', NULL),
(104, 104, 0, '2025-01-12', '2025-12-31');

-- =========================================================
-- gbsapp_paramstable
-- =========================================================
INSERT INTO gbsapp_paramstable (
    id, name, description, valid_from, valid_to, year, value, created, updated
) VALUES
(101, 'ALV', 'Yleinen arvonlisäveroprosentti', '2025-01-01', NULL, 2025, 'ALV 25.5%',1, '2025-01-01 00:00:00', '2025-01-01 00:00:00'),
(102, 'Kilometrikorvaus', 'Oman auton kilometrikorvaus', '2025-01-01', NULL, 2025, 0.57, '2025-01-01 00:00:00', '2025-01-01 00:00:00'),
(103, 'Osapäiväraha', 'Kotimaan osapäiväraha', '2025-01-01', NULL, 2025, 24.00, '2025-01-01 00:00:00', '2025-01-01 00:00:00'),
(104, 'Kokopäiväraha', 'Kotimaan kokopäiväraha', '2025-01-01', NULL, 2025, 51.00, '2025-01-01 00:00:00', '2025-01-01 00:00:00');

-- =========================================================
-- gbsapp_customer
-- =========================================================
INSERT INTO gbsapp_customer (
    id, user_id_id, person_id, custom_role, tax_number, last_name, first_name,
    email, phone, address, postcode, postoffice, tax_rate, bankaccount,
    valid_from, valid_to, created, updated
) VALUES
(101, 101, '010190-123A', 'light entrepreneur', 'FI1234567-8', 'Meikäläinen', 'Matti', 'matti.meikalainen@example.fi', '0401234567', 'Mannerheimintie 12 A 4', '00100', 'Helsinki', 18.50, 'FI2112345600000785', '2025-01-05', NULL, '2025-01-05 09:16:00', '2025-03-01 10:00:00'),
(102, 102, '120285-456B', 'employee', NULL, 'Korhonen', 'Liisa', 'liisa.korhonen@example.fi', '0502345678', 'Hämeenkatu 25 B 7', '33100', 'Tampere', 21.00, 'FI5544332211009988', '2025-01-06', NULL, '2025-01-06 10:05:00', '2025-03-01 10:05:00'),
(103, 103, '230379-789C', 'light entrepreneur', 'FI2345678-9', 'Virtanen', 'Pekka', 'pekka.virtanen@example.fi', '0453456789', 'Kauppakatu 8', '70100', 'Kuopio', 17.50, 'FI1212121212121212', '2025-01-10', NULL, '2025-01-10 08:50:00', '2025-03-01 10:10:00'),
(104, 104, '050992-111D', 'employee', NULL, 'Lahtinen', 'Sari', 'sari.lahtinen@example.fi', '0444567890', 'Satamakatu 3 C 12', '20100', 'Turku', 19.75, 'FI9898989898989898', '2025-01-12', '2025-12-31', '2025-01-12 11:35:00', '2025-03-01 10:15:00');

-- =========================================================
-- gbsapp_companycustomer
-- =========================================================
INSERT INTO gbsapp_companycustomer (
    id, user_id_id, companyId, email, name, contactPerson, phone,
    address, postcode, postoffice, bankaccount, validFrom, validTo, created, updated
) VALUES
(101, 101, '1234567-8', 'ostot@konepajaaurora.fi', 'Konepaja Aurora Oy', 'Tuomas Nieminen', '0201234001', 'Teollisuustie 5', '33800', 'Tampere', 'FI4511112222333344', '2025-01-05', NULL, '2025-01-05 12:00:00', '2025-03-15 08:20:00'),
(102, 102, '2345678-9', 'laskut@jarvimetsa.fi', 'Järvimetsä Rakennus Oy', 'Anna-Maija Lehtonen', '0201234002', 'Sahakuja 9', '80100', 'Joensuu', 'FI9912341234123412', '2025-01-06', NULL, '2025-01-06 12:15:00', '2025-03-15 08:25:00'),
(103, 103, '3456789-0', 'invoice@suomensahkopalvelu.fi', 'Suomen Sähköpalvelu Oy', 'Jari Koskela', '0201234003', 'Virtatie 14', '90100', 'Oulu', 'FI7610101010101010', '2025-01-10', NULL, '2025-01-10 13:30:00', '2025-03-15 08:30:00');

-- =========================================================
-- gbsapp_billigcustomers
-- =========================================================
INSERT INTO gbsapp_billigcustomers (
    id, company_id, company_name, location, contact_person, email, phone,
    address, postcode, postoffice, e_invoice_address, operator_code,
    customer_status, created, updated
) VALUES
(101, '1234567-8', 'Konepaja Aurora Oy', 'Tampere', 'Tuomas Nieminen', 'ostot@konepajaaurora.fi', '0201234001', 'Teollisuustie 5', '33800', 'Tampere', '003712345678', 'BAWCFI22', 'valid', '2025-01-05 12:05:00', '2025-03-20 09:00:00'),
(102, '2345678-9', 'Järvimetsä Rakennus Oy', 'Joensuu', 'Anna-Maija Lehtonen', 'laskut@jarvimetsa.fi', '0201234002', 'Sahakuja 9', '80100', 'Joensuu', '003723456789', 'DABAFIHH', 'valid', '2025-01-06 12:20:00', '2025-03-20 09:05:00'),
(103, '3456789-0', 'Suomen Sähköpalvelu Oy', 'Oulu', 'Jari Koskela', 'invoice@suomensahkopalvelu.fi', '0201234003', 'Virtatie 14', '90100', 'Oulu', '003734567890', 'NDEAFIHH', 'defaulter', '2025-01-10 13:35:00', '2025-03-20 09:10:00'),
(104, '4567890-1', 'Koivuniemi Huolto Oy', 'Espoo', 'Minna Salonen', 'toimisto@koivuniemihuolto.fi', '0201234004', 'Niittytie 2', '02200', 'Espoo', '003745678901', 'HELSFIHH', 'liquidation', '2025-01-15 14:00:00', '2025-03-20 09:15:00');

-- =========================================================
-- gbsapp_billingcase
-- =========================================================
INSERT INTO gbsapp_billingcase (
    id, frontman_cust_id_id, billing_cust_id_id, stage, job_location, job_date,
    job_begin, job_ended, job_hours, work_description, work_task,
    contact_person, phone, email, address, postcode, postoffice,
    billing_method, e_invoice_address, payer_reference, payment,
    vat_percent, group_billing, group_name, number_of_members,
    owner_profit, created, updated
) VALUES
(101, 101, 102, 'invoice sent', 'Tampereen tehdasalue', '2025-03-12', '2025-03-12 08:00:00', '2025-03-12 16:00:00', 8.00, 'Sähkökaapelointien asennus konehallissa', 'Sähköasennus', 'Tuomas Nieminen', '0201234001', 'ostot@konepajaaurora.fi', 'Teollisuustie 5', '33800', 'Tampere', 'verkkolasku', '003712345678', 'AURORA-2025-001', 1480.00, 'ALV 25.5%',1, 0, NULL, 1, 420.00, '2025-03-01 09:00:00', '2025-03-18 10:00:00'),
(102, 103, 101, 'contract accepted', 'Joensuun työmaa', '2025-03-14', '2025-03-14 07:30:00', '2025-03-14 15:30:00', 8.00, 'Rakennustyömaan väliaikaisen sähkökeskuksen huolto', 'Huoltotyö', 'Anna-Maija Lehtonen', '0201234002', 'laskut@jarvimetsa.fi', 'Sahakuja 9', '80100', 'Joensuu', 'sähköposti', NULL, 'JARVI-2025-014', 1320.00,' ALV 25.5%', 1, 'Joensuun huoltoryhmä', 2, 360.00, '2025-03-02 10:15:00', '2025-03-16 14:30:00'),
(103, 102, 104, 'debt collection', 'Oulun toimipiste', '2025-02-28', '2025-02-28 09:00:00', '2025-02-28 17:30:00', 8.50, 'Varastovalaisimien vaihto ja tarkastus', 'Asennus', 'Jari Koskela', '0201234003', 'invoice@suomensahkopalvelu.fi', 'Virtatie 14', '90100', 'Oulu', 'verkkolasku', '003734567890', 'SAHKO-2025-022', 1890.00, 'ALV 25.5%',1, 0, NULL, 1, 510.00, '2025-02-20 08:00:00', '2025-03-25 12:00:00');

-- =========================================================
-- gbsapp_billingcaserow
-- =========================================================
INSERT INTO gbsapp_billingcaserow (
    id, billing_case_id_id, customer_id_id, frontman, work_hours, share_of_pay,
    other_claims, other_claims_amount, travel_exp_claim_id, payroll_id,
    created, updated
) VALUES
(101, 101, 101, 1, 8.00, 100.00, 'Pysäköintimaksu', 12.00, NULL, NULL, '2025-03-12 16:10:00', '2025-03-12 16:10:00'),
(102, 102, 103, 1, 4.00, 50.00, 'Työkalulisä', 25.00, NULL, NULL, '2025-03-14 15:40:00', '2025-03-14 15:40:00'),
(103, 102, 101, 0, 4.00, 50.00, NULL, NULL, NULL, NULL, '2025-03-14 15:41:00', '2025-03-14 15:41:00'),
(104, 103, 102, 1, 8.50, 100.00, 'Nostinvuokra', 85.00, NULL, NULL, '2025-02-28 17:45:00', '2025-02-28 17:45:00');

-- =========================================================
-- gbsapp_contract
-- =========================================================
INSERT INTO gbsapp_contract (
    id, billing_case_id_id, frontman_cust_id_id, billing_cust_id_id,
    contract_nr, contract_date, last_answer_date, contract_status,
    created, updated
) VALUES
(101, 101, 101, 102, 'SOP-2025-001', '2025-03-05', '2025-03-10', 'accepted', '2025-03-05 09:30:00', '2025-03-10 15:00:00'),
(102, 102, 103, 101, 'SOP-2025-002', '2025-03-06', '2025-03-11', 'accepted', '2025-03-06 10:00:00', '2025-03-11 16:15:00'),
(103, 103, 102, 104, 'SOP-2025-003', '2025-02-21', '2025-02-26', 'sent', '2025-02-21 08:30:00', '2025-02-21 08:30:00');

-- =========================================================
-- gbsapp_payroll
-- =========================================================
INSERT INTO gbsapp_payroll (
    id, billing_case_id_id, billing_case_row_id_id, customer_id_id,
    payroll_time, working_hours, gross_salary, tax_rate, tax,
    tt_tyel_proc, tt_tyel, tt_tyottvak_proc, tt_tyottvak,
    net_salary, ta_tyel_proc, ta_tyel, ta_tyottvak_proc,
    ta_tyottvak, acc_insur_proc, acc_insur, payment_date,
    payment_state, created, updated
) VALUES
(101, 101, 101, 101, '03/2025', 8.00, 320.00, 18.50, 59.20, 7.15, 22.88, 0.79, 2.53, 235.39, 17.00, 54.40, 0.20, 0.64, 0.70, 2.24, '2025-03-20', 'paid', '2025-03-15 12:00:00', '2025-03-20 09:00:00'),
(102, 102, 102, 103, '03/2025', 4.00, 180.00, 17.50, 31.50, 7.15, 12.87, 0.79, 1.42, 134.21, 17.00, 30.60, 0.20, 0.36, 0.70, 1.26, '2025-03-21', 'paid', '2025-03-16 12:30:00', '2025-03-21 10:00:00'),
(103, 102, 103, 101, '03/2025', 4.00, 180.00, 18.50, 33.30, 7.15, 12.87, 0.79, 1.42, 132.41, 17.00, 30.60, 0.20, 0.36, 0.70, 1.26, NULL, 'unpaid', '2025-03-16 12:31:00', '2025-03-16 12:31:00'),
(104, 103, 104, 102, '02/2025', 8.50, 365.50, 21.00, 76.76, 7.15, 26.13, 0.79, 2.89, 259.72, 17.00, 62.14, 0.20, 0.73, 0.70, 2.56, NULL, 'unpaid', '2025-03-01 11:00:00', '2025-03-01 11:00:00');

-- =========================================================
-- gbsapp_travelexpenseclaim
-- =========================================================
INSERT INTO gbsapp_travelexpenseclaim (
    id, billing_case_id_id, billing_case_row_id_id, customer_id_id,
    travel_begin, travel_ended, country, itinerary, daily_allowance_type,
    daily_allowance_count, daily_allowance_amount, number_of_km, price_of_km,
    price_of_km_sum, other_expences_desc, other_expences_sum, claims_sum,
    payment_date, payment_state, created, updated
) VALUES
(101, 101, 101, 101, '2025-03-12 06:30:00', '2025-03-12 18:00:00', 'Finland', 'Helsinki - Tampere - Helsinki', 'partial', 1.00, 24.00, 360, 0.570, 205.20, 'Pysäköinti tehdasalueella', 12.00, 241.20, '2025-03-20', 'paid', '2025-03-12 18:10:00', '2025-03-20 09:05:00'),
(102, 102, 102, 103, '2025-03-14 05:45:00', '2025-03-14 18:30:00', 'Finland', 'Kuopio - Joensuu - Kuopio', 'full', 1.00, 51.00, 280, 0.570, 159.60, 'Lounaspysäköinti', 8.50, 219.10, NULL, 'unpaid', '2025-03-14 18:40:00', '2025-03-14 18:40:00'),
(103, 103, 104, 102, '2025-02-28 07:00:00', '2025-02-28 19:30:00', 'Finland', 'Turku - Oulu - Turku', 'full', 1.00, 51.00, 0, NULL, NULL, 'Junaliput ja taksi', 146.80, 197.80, NULL, 'unpaid', '2025-02-28 19:35:00', '2025-02-28 19:35:00');

-- backfill integer reference fields in BillingCaseRow
UPDATE gbsapp_billingcaserow SET travel_exp_claim_id = 101, payroll_id = 101 WHERE id = 101;
UPDATE gbsapp_billingcaserow SET travel_exp_claim_id = 102, payroll_id = 102 WHERE id = 102;
UPDATE gbsapp_billingcaserow SET payroll_id = 103 WHERE id = 103;
UPDATE gbsapp_billingcaserow SET travel_exp_claim_id = 103, payroll_id = 104 WHERE id = 104;

-- =========================================================
-- gbsapp_invoice
-- =========================================================
INSERT INTO gbsapp_invoice (
    id, billing_case_id_id, billing_cust_id_id, invoice_num, invoice_date,
    due_date, invoice_status, description, salary_sum, travel_exp_sum,
    other_claims_sum, amount_vat_0, vat_percent, vat_sum, total_amount,
    reference, bank_account, paid_amount, penalty_interest, payment_date,
    payment_state, created, updated
) VALUES
(101, 101, 102, 'LASKU-2025-001', '2025-03-15', '2025-03-29', 'sent', 'Sähköasennus konehallissa / Konepaja Aurora Oy', 320.00, 241.20, 12.00, 573.20, 'ALV 25.5%',1, 146.17, 719.37, '2025001001', 'FI2112345600000785', 719.37, 0.00, '2025-03-27', 'paid', '2025-03-15 14:00:00', '2025-03-27 08:50:00'),
(102, 102, 101, 'LASKU-2025-002', '2025-03-17', '2025-03-31', 'sent', 'Työmaahuolto / Järvimetsä Rakennus Oy', 360.00, 219.10, 25.00, 604.10, 'ALV 25.5%',1, 154.05, 758.15, '2025001002', 'FI1212121212121212', NULL, 0.00, NULL, 'unpaid', '2025-03-17 13:15:00', '2025-03-17 13:15:00'),
(103, 103, 102, 'LASKU-2025-003', '2025-03-03', '2025-03-17', 'sent', 'Valaisin- ja tarkastustyö / Suomen Sähköpalvelu Oy', 365.50, 197.80, 85.00, 648.30, 'ALV 25.5%',1, 165.32, 813.62, '2025001003', 'FI5544332211009988', 0.00, 12.45, NULL, 'debt_collection', '2025-03-03 10:00:00', '2025-03-25 12:05:00');

-- =========================================================
-- gbsapp_documents
-- =========================================================
INSERT INTO gbsapp_documents (
    id, doc_type, doc_date, user_id_id, contract_id_id, invoice_id_id,
    payroll_id_id, docname, filepath, created, updated
) VALUES
(101, 'tax card', '2025-01-05', 101, NULL, NULL, NULL, 'verokortti_matti_meikalainen_2025.pdf', '/docs/taxcards/verokortti_matti_meikalainen_2025.pdf', '2025-01-05 09:20:00', '2025-01-05 09:20:00'),
(102, 'contract', '2025-03-05', 101, 101, NULL, NULL, 'sopimus_SOP-2025-001.pdf', '/docs/contracts/sopimus_SOP-2025-001.pdf', '2025-03-05 09:35:00', '2025-03-05 09:35:00'),
(103, 'accepted contract', '2025-03-11', 103, 102, NULL, NULL, 'hyvaksytty_sopimus_SOP-2025-002.pdf', '/docs/contracts/hyvaksytty_sopimus_SOP-2025-002.pdf', '2025-03-11 16:20:00', '2025-03-11 16:20:00'),
(104, 'invoice', '2025-03-15', 102, NULL, 101, NULL, 'lasku_LASKU-2025-001.pdf', '/docs/invoices/lasku_LASKU-2025-001.pdf', '2025-03-15 14:05:00', '2025-03-15 14:05:00'),
(105, 'payroll', '2025-03-20', 101, NULL, NULL, 101, 'palkkalaskelma_03_2025_matti.pdf', '/docs/payroll/palkkalaskelma_03_2025_matti.pdf', '2025-03-20 09:10:00', '2025-03-20 09:10:00'),
(106, 'other appendix', '2025-03-14', 103, NULL, NULL, NULL, 'matkalasku_joensuu_2025-03-14.pdf', '/docs/appendices/matkalasku_joensuu_2025-03-14.pdf', '2025-03-14 18:45:00', '2025-03-14 18:45:00');

COMMIT;



-- STILL HUNGRY? Here is some more dummy data
BEGIN TRANSACTION;

INSERT INTO auth_user (
    id, password, last_login, is_superuser, username, last_name,
    email, is_staff, is_active, date_joined, first_name
) VALUES
(107, 'pbkdf2_sha256$600000$dummy$hash107', NULL, 0, 'jari.koskinen@example.fi', 'Koskinen', 'jari.koskinen@example.fi', 0, 1, '2025-02-01 09:00:00', 'Jari'),
(108, 'pbkdf2_sha256$600000$dummy$hash108', NULL, 0, 'anne.heikkinen@example.fi', 'Heikkinen', 'anne.heikkinen@example.fi', 0, 1, '2025-02-01 09:05:00', 'Anne'),
(109, 'pbkdf2_sha256$600000$dummy$hash109', NULL, 0, 'timo.niemi@example.fi', 'Niemi', 'timo.niemi@example.fi', 0, 1, '2025-02-01 09:10:00', 'Timo'),
(110, 'pbkdf2_sha256$600000$dummy$hash110', NULL, 0, 'kaisa.salmi@example.fi', 'Salmi', 'kaisa.salmi@example.fi', 0, 1, '2025-02-01 09:15:00', 'Kaisa'),
(111, 'pbkdf2_sha256$600000$dummy$hash111', NULL, 0, 'olli.rantanen@example.fi', 'Rantanen', 'olli.rantanen@example.fi', 0, 1, '2025-02-01 09:20:00', 'Olli'),
(112, 'pbkdf2_sha256$600000$dummy$hash112', NULL, 0, 'minna.lehto@example.fi', 'Lehto', 'minna.lehto@example.fi', 0, 1, '2025-02-01 09:25:00', 'Minna'),
(113, 'pbkdf2_sha256$600000$dummy$hash113', NULL, 0, 'petri.aalto@example.fi', 'Aalto', 'petri.aalto@example.fi', 0, 1, '2025-02-01 09:30:00', 'Petri'),
(114, 'pbkdf2_sha256$600000$dummy$hash114', NULL, 0, 'laura.hamalainen@example.fi', 'Hämäläinen', 'laura.hamalainen@example.fi', 0, 1, '2025-02-01 09:35:00', 'Laura'),
(115, 'pbkdf2_sha256$600000$dummy$hash115', NULL, 0, 'mikko.seppanen@example.fi', 'Seppänen', 'mikko.seppanen@example.fi', 0, 1, '2025-02-01 09:40:00', 'Mikko'),
(116, 'pbkdf2_sha256$600000$dummy$hash116', NULL, 0, 'riikka.makinen@example.fi', 'Mäkinen', 'riikka.makinen@example.fi', 0, 1, '2025-02-01 09:45:00', 'Riikka'),
(117, 'pbkdf2_sha256$600000$dummy$hash117', NULL, 0, 'sami.laaksonen@example.fi', 'Laaksonen', 'sami.laaksonen@example.fi', 0, 1, '2025-02-01 09:50:00', 'Sami'),
(118, 'pbkdf2_sha256$600000$dummy$hash118', NULL, 0, 'johanna.toivonen@example.fi', 'Toivonen', 'johanna.toivonen@example.fi', 0, 1, '2025-02-01 09:55:00', 'Johanna'),
(119, 'pbkdf2_sha256$600000$dummy$hash119', NULL, 0, 'antti.jokinen@example.fi', 'Jokinen', 'antti.jokinen@example.fi', 0, 1, '2025-02-01 10:00:00', 'Antti'),
(120, 'pbkdf2_sha256$600000$dummy$hash120', NULL, 0, 'elina.saarinen@example.fi', 'Saarinen', 'elina.saarinen@example.fi', 0, 1, '2025-02-01 10:05:00', 'Elina'),
(121, 'pbkdf2_sha256$600000$dummy$hash121', NULL, 0, 'ville.kinnunen@example.fi', 'Kinnunen', 'ville.kinnunen@example.fi', 0, 1, '2025-02-01 10:10:00', 'Ville'),
(122, 'pbkdf2_sha256$600000$dummy$hash122', NULL, 0, 'mari.peltonen@example.fi', 'Peltonen', 'mari.peltonen@example.fi', 0, 1, '2025-02-01 10:15:00', 'Mari'),
(123, 'pbkdf2_sha256$600000$dummy$hash123', NULL, 0, 'juha.hietala@example.fi', 'Hietala', 'juha.hietala@example.fi', 0, 1, '2025-02-01 10:20:00', 'Juha'),
(124, 'pbkdf2_sha256$600000$dummy$hash124', NULL, 0, 'sanna.kuusela@example.fi', 'Kuusela', 'sanna.kuusela@example.fi', 0, 1, '2025-02-01 10:25:00', 'Sanna'),
(125, 'pbkdf2_sha256$600000$dummy$hash125', NULL, 0, 'teemu.nurmi@example.fi', 'Nurmi', 'teemu.nurmi@example.fi', 0, 1, '2025-02-01 10:30:00', 'Teemu'),
(126, 'pbkdf2_sha256$600000$dummy$hash126', NULL, 0, 'paula.karjalainen@example.fi', 'Karjalainen', 'paula.karjalainen@example.fi', 0, 1, '2025-02-01 10:35:00', 'Paula');

INSERT INTO gbsapp_userprofile (
    id, user_id, confirmed, valid_from, valid_to
) VALUES
(107, 107, 1, '2025-02-01', NULL),
(108, 108, 1, '2025-02-01', NULL),
(109, 109, 1, '2025-02-01', NULL),
(110, 110, 1, '2025-02-01', NULL),
(111, 111, 1, '2025-02-01', NULL),
(112, 112, 1, '2025-02-01', NULL),
(113, 113, 1, '2025-02-01', NULL),
(114, 114, 1, '2025-02-01', NULL),
(115, 115, 1, '2025-02-01', NULL),
(116, 116, 1, '2025-02-01', NULL),
(117, 117, 1, '2025-02-01', NULL),
(118, 118, 1, '2025-02-01', NULL),
(119, 119, 1, '2025-02-01', NULL),
(120, 120, 1, '2025-02-01', NULL),
(121, 121, 1, '2025-02-01', NULL),
(122, 122, 1, '2025-02-01', NULL),
(123, 123, 1, '2025-02-01', NULL),
(124, 124, 1, '2025-02-01', NULL),
(125, 125, 1, '2025-02-01', NULL),
(126, 126, 1, '2025-02-01', NULL);

INSERT INTO gbsapp_customer (
    id, user_id_id, person_id, custom_role, tax_number, last_name, first_name,
    email, phone, address, postcode, postoffice, tax_rate, bankaccount,
    valid_from, valid_to, created, updated
) VALUES
(107, 107, '010290-107A', 'employee', NULL, 'Koskinen', 'Jari', 'jari.koskinen@example.fi', '0401234107', 'Mannerheimintie 10 A 2', '00100', 'Helsinki', 17.50, 'FI2012345600000001', '2025-02-01', NULL, '2025-02-01 09:01:00', '2025-03-01 10:00:00'),
(108, 108, '020290-108B', 'light entrepreneur', 'FI1000108-1', 'Heikkinen', 'Anne', 'anne.heikkinen@example.fi', '0411234108', 'Hämeenkatu 20 B 5', '33100', 'Tampere', 18.50, 'FI2112345600000001', '2025-02-01', NULL, '2025-02-01 09:06:00', '2025-03-01 10:05:00'),
(109, 109, '030290-109C', 'employee', NULL, 'Niemi', 'Timo', 'timo.niemi@example.fi', '0421234109', 'Kauppakatu 5', '70100', 'Kuopio', 19.00, 'FI2212345600000001', '2025-02-01', NULL, '2025-02-01 09:11:00', '2025-03-01 10:10:00'),
(110, 110, '040290-110D', 'employee', NULL, 'Salmi', 'Kaisa', 'kaisa.salmi@example.fi', '0431234110', 'Satamakatu 8 C 3', '20100', 'Turku', 20.00, 'FI2312345600000001', '2025-02-01', NULL, '2025-02-01 09:16:00', '2025-03-01 10:15:00'),
(111, 111, '050290-111E', 'light entrepreneur', 'FI1000111-1', 'Rantanen', 'Olli', 'olli.rantanen@example.fi', '0441234111', 'Aleksanterinkatu 15', '90100', 'Oulu', 21.00, 'FI2412345600000001', '2025-02-01', NULL, '2025-02-01 09:21:00', '2025-03-01 10:20:00'),
(112, 112, '060290-112F', 'employee', NULL, 'Lehto', 'Minna', 'minna.lehto@example.fi', '0451234112', 'Keskuskatu 11 A 1', '00100', 'Helsinki', 17.50, 'FI2512345600000001', '2025-02-01', NULL, '2025-02-01 09:26:00', '2025-03-01 10:25:00'),
(113, 113, '070290-113G', 'employee', NULL, 'Aalto', 'Petri', 'petri.aalto@example.fi', '0461234113', 'Puistokatu 7', '20100', 'Turku', 18.50, 'FI2612345600000001', '2025-02-01', NULL, '2025-02-01 09:31:00', '2025-03-01 10:30:00'),
(114, 114, '080290-114H', 'light entrepreneur', 'FI1000114-1', 'Hämäläinen', 'Laura', 'laura.hamalainen@example.fi', '0401234114', 'Torikatu 14', '90100', 'Oulu', 19.00, 'FI2712345600000001', '2025-02-01', NULL, '2025-02-01 09:36:00', '2025-03-01 10:35:00'),
(115, 115, '090290-115I', 'employee', NULL, 'Seppänen', 'Mikko', 'mikko.seppanen@example.fi', '0411234115', 'Rautatienkatu 9', '33100', 'Tampere', 20.00, 'FI2812345600000001', '2025-02-01', NULL, '2025-02-01 09:41:00', '2025-03-01 10:40:00'),
(116, 116, '100290-116J', 'employee', NULL, 'Mäkinen', 'Riikka', 'riikka.makinen@example.fi', '0421234116', 'Snellmaninkatu 6', '70100', 'Kuopio', 21.00, 'FI2912345600000001', '2025-02-01', NULL, '2025-02-01 09:46:00', '2025-03-01 10:45:00'),
(117, 117, '110290-117K', 'light entrepreneur', 'FI1000117-1', 'Laaksonen', 'Sami', 'sami.laaksonen@example.fi', '0431234117', 'Mannerheimintie 10 A 2', '00100', 'Helsinki', 17.50, 'FI3012345600000001', '2025-02-01', NULL, '2025-02-01 09:51:00', '2025-03-01 10:50:00'),
(118, 118, '120290-118L', 'employee', NULL, 'Toivonen', 'Johanna', 'johanna.toivonen@example.fi', '0441234118', 'Hämeenkatu 20 B 5', '33100', 'Tampere', 18.50, 'FI3112345600000001', '2025-02-01', NULL, '2025-02-01 09:56:00', '2025-03-01 10:55:00'),
(119, 119, '130290-119M', 'employee', NULL, 'Jokinen', 'Antti', 'antti.jokinen@example.fi', '0451234119', 'Kauppakatu 5', '70100', 'Kuopio', 19.00, 'FI3212345600000001', '2025-02-01', NULL, '2025-02-01 10:01:00', '2025-03-01 11:00:00'),
(120, 120, '140290-120N', 'light entrepreneur', 'FI1000120-1', 'Saarinen', 'Elina', 'elina.saarinen@example.fi', '0461234120', 'Satamakatu 8 C 3', '20100', 'Turku', 20.00, 'FI3312345600000001', '2025-02-01', NULL, '2025-02-01 10:06:00', '2025-03-01 11:05:00'),
(121, 121, '150290-121O', 'employee', NULL, 'Kinnunen', 'Ville', 'ville.kinnunen@example.fi', '0401234121', 'Aleksanterinkatu 15', '90100', 'Oulu', 21.00, 'FI3412345600000001', '2025-02-01', NULL, '2025-02-01 10:11:00', '2025-03-01 11:10:00'),
(122, 122, '160290-122P', 'employee', NULL, 'Peltonen', 'Mari', 'mari.peltonen@example.fi', '0411234122', 'Keskuskatu 11 A 1', '00100', 'Helsinki', 17.50, 'FI3512345600000001', '2025-02-01', NULL, '2025-02-01 10:16:00', '2025-03-01 11:15:00'),
(123, 123, '170290-123Q', 'light entrepreneur', 'FI1000123-1', 'Hietala', 'Juha', 'juha.hietala@example.fi', '0421234123', 'Puistokatu 7', '20100', 'Turku', 18.50, 'FI3612345600000001', '2025-02-01', NULL, '2025-02-01 10:21:00', '2025-03-01 11:20:00'),
(124, 124, '180290-124R', 'employee', NULL, 'Kuusela', 'Sanna', 'sanna.kuusela@example.fi', '0431234124', 'Torikatu 14', '90100', 'Oulu', 19.00, 'FI3712345600000001', '2025-02-01', NULL, '2025-02-01 10:26:00', '2025-03-01 11:25:00'),
(125, 125, '190290-125S', 'employee', NULL, 'Nurmi', 'Teemu', 'teemu.nurmi@example.fi', '0441234125', 'Rautatienkatu 9', '33100', 'Tampere', 20.00, 'FI3812345600000001', '2025-02-01', NULL, '2025-02-01 10:31:00', '2025-03-01 11:30:00'),
(126, 126, '200290-126T', 'light entrepreneur', 'FI1000126-1', 'Karjalainen', 'Paula', 'paula.karjalainen@example.fi', '0451234126', 'Snellmaninkatu 6', '70100', 'Kuopio', 21.00, 'FI3912345600000001', '2025-02-01', NULL, '2025-02-01 10:36:00', '2025-03-01 11:35:00');

INSERT INTO gbsapp_companycustomer (
    id, user_id_id, companyId, email, name, contactPerson, phone,
    address, postcode, postoffice, bankaccount, validFrom, validTo, created, updated
) VALUES
(107, 107, '5566778-1', 'ostot@pohjolanrakennus.fi', 'Pohjolan Rakennus Oy', 'Jari Koskinen', '0201111111', 'Rakennustie 1', '00100', 'Helsinki', 'FI4011112222333345', '2025-02-03', NULL, '2025-02-03 12:00:00', '2025-03-15 08:00:00'),
(108, 108, '6677889-2', 'laskut@arktislogistiikka.fi', 'Arktis Logistiikka Oy', 'Anne Heikkinen', '0202222222', 'Logistiikkatie 2', '33100', 'Tampere', 'FI4111112222333345', '2025-02-03', NULL, '2025-02-03 12:05:00', '2025-03-15 08:05:00'),
(109, 109, '7788990-3', 'invoice@savonsahkohuolto.fi', 'Savon Sähköhuolto Oy', 'Timo Niemi', '0203333333', 'Sähkötie 3', '70100', 'Kuopio', 'FI4211112222333345', '2025-02-03', NULL, '2025-02-03 12:10:00', '2025-03-15 08:10:00'),
(110, 110, '8899001-4', 'toimisto@turunkiinteistoapu.fi', 'Turun Kiinteistöapu Oy', 'Kaisa Salmi', '0204444444', 'Huoltotie 4', '20100', 'Turku', 'FI4311112222333345', '2025-02-03', NULL, '2025-02-03 12:15:00', '2025-03-15 08:15:00'),
(111, 111, '9900112-5', 'ostot@oulunteollisuuspalvelu.fi', 'Oulun Teollisuuspalvelu Oy', 'Olli Rantanen', '0205555555', 'Teollisuustie 5', '90100', 'Oulu', 'FI4411112222333345', '2025-02-03', NULL, '2025-02-03 12:20:00', '2025-03-15 08:20:00'),
(112, 112, '1122334-6', 'laskut@jarvimaaninfra.fi', 'Järvimaan Infra Oy', 'Minna Lehto', '0206666666', 'Työmaakuja 6', '80100', 'Joensuu', 'FI4511112222333345', '2025-02-03', NULL, '2025-02-03 12:25:00', '2025-03-15 08:25:00'),
(113, 113, '2233445-7', 'ostot@kskoneasennus.fi', 'Keski-Suomen Koneasennus Oy', 'Petri Aalto', '0207777777', 'Asennustie 7', '40100', 'Jyväskylä', 'FI4611112222333345', '2025-02-03', NULL, '2025-02-03 12:30:00', '2025-03-15 08:30:00'),
(114, 114, '3344556-8', 'invoice@lapinhuoltorengas.fi', 'Lapin Huoltorengas Oy', 'Laura Hämäläinen', '0208888888', 'Korjaamokuja 8', '96100', 'Rovaniemi', 'FI4711112222333345', '2025-02-03', NULL, '2025-02-03 12:35:00', '2025-03-15 08:35:00'),
(115, 115, '4455667-9', 'toimisto@saimaanlvi.fi', 'Saimaan LVI-Palvelu Oy', 'Mikko Seppänen', '0209999999', 'Putkitie 9', '53100', 'Lappeenranta', 'FI4811112222333345', '2025-02-03', NULL, '2025-02-03 12:40:00', '2025-03-15 08:40:00'),
(116, 116, '5566880-0', 'laskut@uudenmaansahkotiimi.fi', 'Uudenmaan Sähkötiimi Oy', 'Riikka Mäkinen', '0201010101', 'Kaapelitie 10', '01300', 'Vantaa', 'FI4911112222333345', '2025-02-03', NULL, '2025-02-03 12:45:00', '2025-03-15 08:45:00');

INSERT INTO gbsapp_billigcustomers (
    id, company_id, company_name, location, contact_person, email, phone,
    address, postcode, postoffice, e_invoice_address, operator_code,
    customer_status, created, updated
) VALUES
(107, '5566778-1', 'Pohjolan Rakennus Oy', 'Helsinki', 'Jari Koskinen', 'ostot@pohjolanrakennus.fi', '0201111111', 'Rakennustie 1', '00100', 'Helsinki', '003755667781', 'HELSFIHH', 'valid', '2025-02-03 12:00:00', '2025-03-15 08:00:00'),
(108, '6677889-2', 'Arktis Logistiikka Oy', 'Tampere', 'Anne Heikkinen', 'laskut@arktislogistiikka.fi', '0202222222', 'Logistiikkatie 2', '33100', 'Tampere', '003766778892', 'NDEAFIHH', 'valid', '2025-02-03 12:05:00', '2025-03-15 08:05:00'),
(109, '7788990-3', 'Savon Sähköhuolto Oy', 'Kuopio', 'Timo Niemi', 'invoice@savonsahkohuolto.fi', '0203333333', 'Sähkötie 3', '70100', 'Kuopio', '003777889903', 'DABAFIHH', 'defaulter', '2025-02-03 12:10:00', '2025-03-15 08:10:00'),
(110, '8899001-4', 'Turun Kiinteistöapu Oy', 'Turku', 'Kaisa Salmi', 'toimisto@turunkiinteistoapu.fi', '0204444444', 'Huoltotie 4', '20100', 'Turku', '003788990014', 'ITELFIHH', 'valid', '2025-02-03 12:15:00', '2025-03-15 08:15:00'),
(111, '9900112-5', 'Oulun Teollisuuspalvelu Oy', 'Oulu', 'Olli Rantanen', 'ostot@oulunteollisuuspalvelu.fi', '0205555555', 'Teollisuustie 5', '90100', 'Oulu', '003799001125', 'OKOYFIHH', 'liquidation', '2025-02-03 12:20:00', '2025-03-15 08:20:00'),
(112, '1122334-6', 'Järvimaan Infra Oy', 'Joensuu', 'Minna Lehto', 'laskut@jarvimaaninfra.fi', '0206666666', 'Työmaakuja 6', '80100', 'Joensuu', '003711223346', 'HELSFIHH', 'valid', '2025-02-03 12:25:00', '2025-03-15 08:25:00'),
(113, '2233445-7', 'Keski-Suomen Koneasennus Oy', 'Jyväskylä', 'Petri Aalto', 'ostot@kskoneasennus.fi', '0207777777', 'Asennustie 7', '40100', 'Jyväskylä', '003722334457', 'NDEAFIHH', 'valid', '2025-02-03 12:30:00', '2025-03-15 08:30:00'),
(114, '3344556-8', 'Lapin Huoltorengas Oy', 'Rovaniemi', 'Laura Hämäläinen', 'invoice@lapinhuoltorengas.fi', '0208888888', 'Korjaamokuja 8', '96100', 'Rovaniemi', '003733445568', 'DABAFIHH', 'bankruptcy', '2025-02-03 12:35:00', '2025-03-15 08:35:00'),
(115, '4455667-9', 'Saimaan LVI-Palvelu Oy', 'Lappeenranta', 'Mikko Seppänen', 'toimisto@saimaanlvi.fi', '0209999999', 'Putkitie 9', '53100', 'Lappeenranta', '003744556679', 'HELSFIHH', 'ceased_operations', '2025-02-03 12:40:00', '2025-03-15 08:40:00'),
(116, '5566880-0', 'Uudenmaan Sähkötiimi Oy', 'Vantaa', 'Riikka Mäkinen', 'laskut@uudenmaansahkotiimi.fi', '0201010101', 'Kaapelitie 10', '01300', 'Vantaa', '003755668800', 'NDEAFIHH', 'valid', '2025-02-03 12:45:00', '2025-03-15 08:45:00');

INSERT INTO gbsapp_billingcase (
    id, frontman_cust_id_id, billing_cust_id_id, stage, job_location, job_date,
    job_begin, job_ended, job_hours, work_description, work_task,
    contact_person, phone, email, address, postcode, postoffice,
    billing_method, e_invoice_address, payer_reference, payment,
    vat_percent,vat_includes,group_billing, group_name, number_of_members,
    owner_profit, created, updated
) VALUES
(107, 107, 108, 'invoice sent', 'Helsinki työmaa', '2025-03-10', '2025-03-10 08:00:00', '2025-03-10 16:30:00', 8.50, 'Sähkökeskuksen huolto ja tarkastus', 'Sähköasennus', 'Jari Koskinen', '0201111111', 'ostot@pohjolanrakennus.fi', 'Rakennustie 1', '00100', 'Helsinki', 'verkkolasku', '003755667781', 'REF-2025-107', 1280.00, 'ALV 25.5%',1, 0, NULL, 1, 358.40, '2025-03-01 09:00:00', '2025-03-18 10:00:00'),
(108, 108, 109, 'contract accepted', 'Tampere työmaa', '2025-03-11', '2025-03-11 08:00:00', '2025-03-11 16:00:00', 8.00, 'Varastovalaistuksen asennus', 'Huoltotyö', 'Anne Heikkinen', '0202222222', 'laskut@arktislogistiikka.fi', 'Logistiikkatie 2', '33100', 'Tampere', 'sähköposti', NULL, 'REF-2025-108', 1375.00, 'ALV 25.5%',1, 1, 'Tampere huoltoryhmä', 2, 385.00, '2025-03-02 09:00:00', '2025-03-19 10:00:00'),
(109, 109, 110, 'debt collection', 'Kuopio työmaa', '2025-03-12', '2025-03-12 08:00:00', '2025-03-12 16:00:00', 8.00, 'Kaapelointityö tuotantolinjalla', 'Asennus', 'Timo Niemi', '0203333333', 'invoice@savonsahkohuolto.fi', 'Sähkötie 3', '70100', 'Kuopio', 'verkkolasku', '003777889903', 'REF-2025-109', 1470.00, 'ALV 25.5%',1,1, 0, NULL, 1, 411.60, '2025-03-03 09:00:00', '2025-03-20 10:00:00'),
(110, 110, 111, 'invoice paid', 'Turku työmaa', '2025-03-13', '2025-03-13 08:00:00', '2025-03-13 16:30:00', 8.50, 'Kiinteistötekniikan vikakorjaus', 'Tarkastus', 'Kaisa Salmi', '0204444444', 'toimisto@turunkiinteistoapu.fi', 'Huoltotie 4', '20100', 'Turku', 'sähköposti', NULL, 'REF-2025-110', 1565.00, 'ALV 25.5%',1,1, 0, NULL, 1, 438.20, '2025-03-04 09:00:00', '2025-03-21 10:00:00'),
(111, 111, 112, 'invoice sent', 'Oulu työmaa', '2025-03-14', '2025-03-14 08:00:00', '2025-03-14 16:00:00', 8.00, 'Sähkökeskuksen huolto ja tarkastus', 'Sähköasennus', 'Olli Rantanen', '0205555555', 'ostot@oulunteollisuuspalvelu.fi', 'Teollisuustie 5', '90100', 'Oulu', 'verkkolasku', '003799001125', 'REF-2025-111', 1660.00, 'ALV 25.5%',1, 1, 'Oulu huoltoryhmä', 2, 464.80, '2025-03-05 09:00:00', '2025-03-22 10:00:00'),
(112, 112, 113, 'contract accepted', 'Joensuu työmaa', '2025-03-15', '2025-03-15 08:00:00', '2025-03-15 16:00:00', 8.00, 'Varastovalaistuksen asennus', 'Huoltotyö', 'Minna Lehto', '0206666666', 'laskut@jarvimaaninfra.fi', 'Työmaakuja 6', '80100', 'Joensuu', 'sähköposti', NULL, 'REF-2025-112', 1755.00, 'ALV 25.5%',1, 0, NULL, 1, 491.40, '2025-03-06 09:00:00', '2025-03-23 10:00:00'),
(113, 113, 114, 'debt collection', 'Jyväskylä työmaa', '2025-03-16', '2025-03-16 08:00:00', '2025-03-16 16:30:00', 8.50, 'Kaapelointityö tuotantolinjalla', 'Asennus', 'Petri Aalto', '0207777777', 'ostot@kskoneasennus.fi', 'Asennustie 7', '40100', 'Jyväskylä', 'verkkolasku', '003722334457', 'REF-2025-113', 1850.00, 'ALV 25.5%',1, 0, NULL, 1, 518.00, '2025-03-07 09:00:00', '2025-03-24 10:00:00'),
(114, 114, 115, 'invoice paid', 'Rovaniemi työmaa', '2025-03-17', '2025-03-17 08:00:00', '2025-03-17 16:00:00', 8.00, 'Kiinteistötekniikan vikakorjaus', 'Tarkastus', 'Laura Hämäläinen', '0208888888', 'invoice@lapinhuoltorengas.fi', 'Korjaamokuja 8', '96100', 'Rovaniemi', 'sähköposti', NULL, 'REF-2025-114', 1945.00, 'ALV 25.5%',1, 1, 'Rovaniemi huoltoryhmä', 2, 544.60, '2025-03-08 09:00:00', '2025-03-25 10:00:00'),
(115, 115, 116, 'invoice sent', 'Lappeenranta työmaa', '2025-03-18', '2025-03-18 08:00:00', '2025-03-18 16:00:00', 8.00, 'Sähkökeskuksen huolto ja tarkastus', 'Sähköasennus', 'Mikko Seppänen', '0209999999', 'toimisto@saimaanlvi.fi', 'Putkitie 9', '53100', 'Lappeenranta', 'verkkolasku', '003744556679', 'REF-2025-115', 2040.00, 'ALV 25.5%',1, 0, NULL, 1, 571.20, '2025-03-09 09:00:00', '2025-03-26 10:00:00'),
(116, 116, 117, 'contract accepted', 'Vantaa työmaa', '2025-03-19', '2025-03-19 08:00:00', '2025-03-19 16:30:00', 8.50, 'Varastovalaistuksen asennus', 'Huoltotyö', 'Riikka Mäkinen', '0201010101', 'laskut@uudenmaansahkotiimi.fi', 'Kaapelitie 10', '01300', 'Vantaa', 'sähköposti', NULL, 'REF-2025-116', 2135.00, 'ALV 25.5%',1, 0, NULL, 1, 597.80, '2025-03-10 09:00:00', '2025-03-27 10:00:00'),
(117, 117, 118, 'debt collection', 'Helsinki työmaa', '2025-03-20', '2025-03-20 08:00:00', '2025-03-20 16:00:00', 8.00, 'Kaapelointityö tuotantolinjalla', 'Asennus', 'Jari Koskinen', '0201111111', 'ostot@pohjolanrakennus.fi', 'Rakennustie 1', '00100', 'Helsinki', 'verkkolasku', '003755667781', 'REF-2025-117', 2230.00, 'ALV 25.5%',1, 1, 'Helsinki huoltoryhmä', 2, 624.40, '2025-03-11 09:00:00', '2025-03-28 10:00:00'),
(118, 118, 119, 'invoice paid', 'Tampere työmaa', '2025-03-21', '2025-03-21 08:00:00', '2025-03-21 16:00:00', 8.00, 'Kiinteistötekniikan vikakorjaus', 'Tarkastus', 'Anne Heikkinen', '0202222222', 'laskut@arktislogistiikka.fi', 'Logistiikkatie 2', '33100', 'Tampere', 'sähköposti', NULL, 'REF-2025-118', 2325.00, 'ALV 25.5%',1, 0, NULL, 1, 651.00, '2025-03-12 09:00:00', '2025-03-29 10:00:00');

INSERT INTO gbsapp_billingcaserow (
    id, billing_case_id_id, customer_id_id, frontman, work_hours, share_of_pay,
    other_claims, other_claims_amount, travel_exp_claim_id, payroll_id,
    created, updated
) VALUES
(107, 107, 107, 1, 8.50, 100.00, 'Pysäköintimaksu', 12.0, NULL, NULL, '2025-03-12 16:10:00', '2025-03-12 16:10:00'),
(108, 108, 108, 1, 4.00, 50.00, 'Pysäköintimaksu', 12.0, NULL, NULL, '2025-03-13 16:10:00', '2025-03-13 16:10:00'),
(109, 108, 109, 0, 4.00, 50.00, 'Työkalulisä', 25.0, NULL, NULL, '2025-03-13 16:11:00', '2025-03-13 16:11:00'),
(110, 109, 109, 1, 8.00, 100.00, 'Pysäköintimaksu', 12.0, NULL, NULL, '2025-03-14 16:10:00', '2025-03-14 16:10:00'),
(111, 110, 110, 1, 8.50, 100.00, 'Pysäköintimaksu', 12.0, NULL, NULL, '2025-03-15 16:10:00', '2025-03-15 16:10:00'),
(112, 111, 111, 1, 4.00, 50.00, 'Pysäköintimaksu', 12.0, NULL, NULL, '2025-03-16 16:10:00', '2025-03-16 16:10:00'),
(113, 111, 112, 0, 4.00, 50.00, 'Työkalulisä', 25.0, NULL, NULL, '2025-03-16 16:11:00', '2025-03-16 16:11:00'),
(114, 112, 112, 1, 8.00, 100.00, 'Pysäköintimaksu', 12.0, NULL, NULL, '2025-03-17 16:10:00', '2025-03-17 16:10:00'),
(115, 113, 113, 1, 8.50, 100.00, 'Pysäköintimaksu', 12.0, NULL, NULL, '2025-03-18 16:10:00', '2025-03-18 16:10:00'),
(116, 114, 114, 1, 4.00, 50.00, 'Pysäköintimaksu', 12.0, NULL, NULL, '2025-03-19 16:10:00', '2025-03-19 16:10:00'),
(117, 114, 115, 0, 4.00, 50.00, 'Työkalulisä', 25.0, NULL, NULL, '2025-03-19 16:11:00', '2025-03-19 16:11:00'),
(118, 115, 115, 1, 8.00, 100.00, 'Pysäköintimaksu', 12.0, NULL, NULL, '2025-03-20 16:10:00', '2025-03-20 16:10:00'),
(119, 116, 116, 1, 8.50, 100.00, 'Pysäköintimaksu', 12.0, NULL, NULL, '2025-03-21 16:10:00', '2025-03-21 16:10:00'),
(120, 117, 117, 1, 4.00, 50.00, 'Pysäköintimaksu', 12.0, NULL, NULL, '2025-03-22 16:10:00', '2025-03-22 16:10:00'),
(121, 117, 118, 0, 4.00, 50.00, 'Työkalulisä', 25.0, NULL, NULL, '2025-03-22 16:11:00', '2025-03-22 16:11:00'),
(122, 118, 118, 1, 8.00, 100.00, 'Pysäköintimaksu', 12.0, NULL, NULL, '2025-03-23 16:10:00', '2025-03-23 16:10:00');

INSERT INTO gbsapp_contract (
    id, billing_case_id_id, frontman_cust_id_id, billing_cust_id_id,
    contract_nr, contract_date, last_answer_date, contract_status,
    created, updated
) VALUES
(107, 107, 107, 108, 'SOP-2025-107', '2025-03-05', '2025-03-10', 'accepted', '2025-03-05 09:30:00', '2025-03-05 09:30:00'),
(108, 108, 108, 109, 'SOP-2025-108', '2025-03-06', '2025-03-11', 'sent', '2025-03-06 09:30:00', '2025-03-06 09:30:00'),
(109, 109, 109, 110, 'SOP-2025-109', '2025-03-07', '2025-03-12', 'accepted', '2025-03-07 09:30:00', '2025-03-07 09:30:00'),
(110, 110, 110, 111, 'SOP-2025-110', '2025-03-08', '2025-03-13', 'rejected', '2025-03-08 09:30:00', '2025-03-08 09:30:00'),
(111, 111, 111, 112, 'SOP-2025-111', '2025-03-09', '2025-03-14', 'accepted', '2025-03-09 09:30:00', '2025-03-09 09:30:00'),
(112, 112, 112, 113, 'SOP-2025-112', '2025-03-10', '2025-03-15', 'sent', '2025-03-10 09:30:00', '2025-03-10 09:30:00'),
(113, 113, 113, 114, 'SOP-2025-113', '2025-03-11', '2025-03-16', 'accepted', '2025-03-11 09:30:00', '2025-03-11 09:30:00'),
(114, 114, 114, 115, 'SOP-2025-114', '2025-03-12', '2025-03-17', 'rejected', '2025-03-12 09:30:00', '2025-03-12 09:30:00'),
(115, 115, 115, 116, 'SOP-2025-115', '2025-03-13', '2025-03-18', 'accepted', '2025-03-13 09:30:00', '2025-03-13 09:30:00'),
(116, 116, 116, 117, 'SOP-2025-116', '2025-03-14', '2025-03-19', 'sent', '2025-03-14 09:30:00', '2025-03-14 09:30:00'),
(117, 117, 117, 118, 'SOP-2025-117', '2025-03-15', '2025-03-20', 'accepted', '2025-03-15 09:30:00', '2025-03-15 09:30:00'),
(118, 118, 118, 119, 'SOP-2025-118', '2025-03-16', '2025-03-21', 'rejected', '2025-03-16 09:30:00', '2025-03-16 09:30:00');

INSERT INTO gbsapp_payroll (
    id, billing_case_id_id, billing_case_row_id_id, customer_id_id,
    payroll_time, working_hours, gross_salary, tax_rate, tax,
    tt_tyel_proc, tt_tyel, tt_tyottvak_proc, tt_tyottvak,
    net_salary, ta_tyel_proc, ta_tyel, ta_tyottvak_proc,
    ta_tyottvak, acc_insur_proc, acc_insur, payment_date,
    payment_state, created, updated
) VALUES
(107, 107, 107, 107, '03/2025', 8.50, 357.00, 17.50, 62.48, 7.15, 25.53, 0.79, 2.82, 266.17, 17.00, 60.69, 0.20, 0.71, 0.70, 2.50, '2025-03-20', 'paid', '2025-03-15 12:00:00', '2025-03-15 12:00:00'),
(108, 108, 108, 108, '03/2025', 4.00, 168.00, 18.50, 31.08, 7.15, 12.01, 0.79, 1.33, 123.58, 17.00, 28.56, 0.20, 0.34, 0.70, 1.18, NULL, 'unpaid', '2025-03-16 12:00:00', '2025-03-16 12:00:00'),
(109, 108, 109, 109, '03/2025', 4.00, 183.00, 19.00, 34.77, 7.15, 13.08, 0.79, 1.45, 133.70, 17.00, 31.11, 0.20, 0.37, 0.70, 1.28, NULL, 'unpaid', '2025-03-16 12:01:00', '2025-03-16 12:01:00'),
(110, 109, 110, 109, '03/2025', 8.00, 336.00, 19.00, 63.84, 7.15, 24.02, 0.79, 2.65, 245.49, 17.00, 57.12, 0.20, 0.67, 0.70, 2.35, NULL, 'unpaid', '2025-03-17 12:00:00', '2025-03-17 12:00:00'),
(111, 110, 111, 110, '03/2025', 8.50, 357.00, 20.00, 71.40, 7.15, 25.53, 0.79, 2.82, 257.25, 17.00, 60.69, 0.20, 0.71, 0.70, 2.50, '2025-03-23', 'paid', '2025-03-18 12:00:00', '2025-03-18 12:00:00'),
(112, 111, 112, 111, '03/2025', 4.00, 168.00, 21.00, 35.28, 7.15, 12.01, 0.79, 1.33, 119.38, 17.00, 28.56, 0.20, 0.34, 0.70, 1.18, NULL, 'unpaid', '2025-03-19 12:00:00', '2025-03-19 12:00:00'),
(113, 111, 113, 112, '03/2025', 4.00, 183.00, 17.50, 32.02, 7.15, 13.08, 0.79, 1.45, 136.45, 17.00, 31.11, 0.20, 0.37, 0.70, 1.28, NULL, 'unpaid', '2025-03-19 12:01:00', '2025-03-19 12:01:00'),
(114, 112, 114, 112, '03/2025', 8.00, 336.00, 17.50, 58.80, 7.15, 24.02, 0.79, 2.65, 250.53, 17.00, 57.12, 0.20, 0.67, 0.70, 2.35, NULL, 'unpaid', '2025-03-20 12:00:00', '2025-03-20 12:00:00'),
(115, 113, 115, 113, '03/2025', 8.50, 357.00, 18.50, 66.05, 7.15, 25.53, 0.79, 2.82, 262.60, 17.00, 60.69, 0.20, 0.71, 0.70, 2.50, '2025-03-26', 'paid', '2025-03-21 12:00:00', '2025-03-21 12:00:00'),
(116, 114, 116, 114, '03/2025', 4.00, 168.00, 19.00, 31.92, 7.15, 12.01, 0.79, 1.33, 122.74, 17.00, 28.56, 0.20, 0.34, 0.70, 1.18, NULL, 'unpaid', '2025-03-22 12:00:00', '2025-03-22 12:00:00'),
(117, 114, 117, 115, '03/2025', 4.00, 183.00, 20.00, 36.60, 7.15, 13.08, 0.79, 1.45, 131.87, 17.00, 31.11, 0.20, 0.37, 0.70, 1.28, NULL, 'unpaid', '2025-03-22 12:01:00', '2025-03-22 12:01:00'),
(118, 115, 118, 115, '03/2025', 8.00, 336.00, 20.00, 67.20, 7.15, 24.02, 0.79, 2.65, 242.13, 17.00, 57.12, 0.20, 0.67, 0.70, 2.35, NULL, 'unpaid', '2025-03-23 12:00:00', '2025-03-23 12:00:00'),
(119, 116, 119, 116, '03/2025', 8.50, 357.00, 21.00, 74.97, 7.15, 25.53, 0.79, 2.82, 253.68, 17.00, 60.69, 0.20, 0.71, 0.70, 2.50, '2025-03-29', 'paid', '2025-03-24 12:00:00', '2025-03-24 12:00:00'),
(120, 117, 120, 117, '03/2025', 4.00, 168.00, 17.50, 29.40, 7.15, 12.01, 0.79, 1.33, 125.26, 17.00, 28.56, 0.20, 0.34, 0.70, 1.18, NULL, 'unpaid', '2025-03-25 12:00:00', '2025-03-25 12:00:00'),
(121, 117, 121, 118, '03/2025', 4.00, 183.00, 18.50, 33.85, 7.15, 13.08, 0.79, 1.45, 134.62, 17.00, 31.11, 0.20, 0.37, 0.70, 1.28, NULL, 'unpaid', '2025-03-25 12:01:00', '2025-03-25 12:01:00'),
(122, 118, 122, 118, '03/2025', 8.00, 336.00, 18.50, 62.16, 7.15, 24.02, 0.79, 2.65, 247.17, 17.00, 57.12, 0.20, 0.67, 0.70, 2.35, NULL, 'unpaid', '2025-03-26 12:00:00', '2025-03-26 12:00:00');

INSERT INTO gbsapp_travelexpenseclaim (
    id, billing_case_id_id, billing_case_row_id_id, customer_id_id,
    travel_begin, travel_ended, country, itinerary, daily_allowance_type,
    daily_allowance_count, daily_allowance_amount, number_of_km, price_of_km,
    price_of_km_sum, other_expences_desc, other_expences_sum, claims_sum,
    payment_date, payment_state, created, updated
) VALUES
(107, 107, 107, 107, '2025-03-10 06:30:00', '2025-03-10 18:30:00', 'Finland', 'Helsinki - Helsinki - Helsinki', 'partial', 1.00, 24.00, 180, 0.570, 102.60, 'Pysäköinti työmaalla', 12.00, 138.60, '2025-03-20', 'paid', '2025-03-12 18:10:00', '2025-03-12 18:10:00'),
(108, 108, 108, 108, '2025-03-11 06:30:00', '2025-03-11 18:00:00', 'Finland', 'Helsinki - Tampere - Helsinki', 'full', 1.00, 51.00, 192, 0.570, 109.44, 'Pysäköinti työmaalla', 12.00, 172.44, NULL, 'unpaid', '2025-03-13 18:10:00', '2025-03-13 18:10:00'),
(109, 108, 109, 109, '2025-03-11 06:30:00', '2025-03-11 18:00:00', 'Finland', 'Tampere paikallinen siirtymä', 'full', 1.00, 51.00, NULL, NULL, NULL, 'Lounaspysäköinti', 8.50, 59.50, NULL, 'unpaid', '2025-03-13 18:11:00', '2025-03-13 18:11:00'),
(110, 109, 110, 109, '2025-03-12 06:30:00', '2025-03-12 18:00:00', 'Finland', 'Helsinki - Kuopio - Helsinki', 'partial', 1.00, 24.00, 204, 0.570, 116.28, 'Pysäköinti työmaalla', 12.00, 152.28, NULL, 'unpaid', '2025-03-14 18:10:00', '2025-03-14 18:10:00'),
(111, 110, 111, 110, '2025-03-13 06:30:00', '2025-03-13 18:30:00', 'Finland', 'Helsinki - Turku - Helsinki', 'full', 1.00, 51.00, 216, 0.570, 123.12, 'Pysäköinti työmaalla', 12.00, 186.12, '2025-03-23', 'paid', '2025-03-15 18:10:00', '2025-03-15 18:10:00'),
(112, 111, 112, 111, '2025-03-14 06:30:00', '2025-03-14 18:00:00', 'Finland', 'Helsinki - Oulu - Helsinki', 'partial', 1.00, 24.00, 228, 0.570, 129.96, 'Pysäköinti työmaalla', 12.00, 165.96, NULL, 'unpaid', '2025-03-16 18:10:00', '2025-03-16 18:10:00'),
(113, 111, 113, 112, '2025-03-14 06:30:00', '2025-03-14 18:00:00', 'Finland', 'Oulu paikallinen siirtymä', 'partial', 1.00, 24.00, NULL, NULL, NULL, 'Lounaspysäköinti', 8.50, 32.50, NULL, 'unpaid', '2025-03-16 18:11:00', '2025-03-16 18:11:00'),
(114, 112, 114, 112, '2025-03-15 06:30:00', '2025-03-15 18:00:00', 'Finland', 'Helsinki - Joensuu - Helsinki', 'full', 1.00, 51.00, 240, 0.570, 136.80, 'Pysäköinti työmaalla', 12.00, 199.80, NULL, 'unpaid', '2025-03-17 18:10:00', '2025-03-17 18:10:00'),
(115, 113, 115, 113, '2025-03-16 06:30:00', '2025-03-16 18:30:00', 'Finland', 'Helsinki - Jyväskylä - Helsinki', 'partial', 1.00, 24.00, 252, 0.570, 143.64, 'Pysäköinti työmaalla', 12.00, 179.64, '2025-03-26', 'paid', '2025-03-18 18:10:00', '2025-03-18 18:10:00'),
(116, 114, 116, 114, '2025-03-17 06:30:00', '2025-03-17 18:00:00', 'Finland', 'Helsinki - Rovaniemi - Helsinki', 'full', 1.00, 51.00, 264, 0.570, 150.48, 'Pysäköinti työmaalla', 12.00, 213.48, NULL, 'unpaid', '2025-03-19 18:10:00', '2025-03-19 18:10:00'),
(117, 114, 117, 115, '2025-03-17 06:30:00', '2025-03-17 18:00:00', 'Finland', 'Rovaniemi paikallinen siirtymä', 'full', 1.00, 51.00, NULL, NULL, NULL, 'Lounaspysäköinti', 8.50, 59.50, NULL, 'unpaid', '2025-03-19 18:11:00', '2025-03-19 18:11:00'),
(118, 115, 118, 115, '2025-03-18 06:30:00', '2025-03-18 18:00:00', 'Finland', 'Helsinki - Lappeenranta - Helsinki', 'partial', 1.00, 24.00, 276, 0.570, 157.32, 'Pysäköinti työmaalla', 12.00, 193.32, NULL, 'unpaid', '2025-03-20 18:10:00', '2025-03-20 18:10:00'),
(119, 116, 119, 116, '2025-03-19 06:30:00', '2025-03-19 18:30:00', 'Finland', 'Helsinki - Vantaa - Helsinki', 'full', 1.00, 51.00, 288, 0.570, 164.16, 'Pysäköinti työmaalla', 12.00, 227.16, '2025-03-29', 'paid', '2025-03-21 18:10:00', '2025-03-21 18:10:00'),
(120, 117, 120, 117, '2025-03-20 06:30:00', '2025-03-20 18:00:00', 'Finland', 'Helsinki - Helsinki - Helsinki', 'partial', 1.00, 24.00, 300, 0.570, 171.00, 'Pysäköinti työmaalla', 12.00, 207.00, NULL, 'unpaid', '2025-03-22 18:10:00', '2025-03-22 18:10:00'),
(121, 117, 121, 118, '2025-03-20 06:30:00', '2025-03-20 18:00:00', 'Finland', 'Helsinki paikallinen siirtymä', 'partial', 1.00, 24.00, NULL, NULL, NULL, 'Lounaspysäköinti', 8.50, 32.50, NULL, 'unpaid', '2025-03-22 18:11:00', '2025-03-22 18:11:00'),
(122, 118, 122, 118, '2025-03-21 06:30:00', '2025-03-21 18:00:00', 'Finland', 'Helsinki - Tampere - Helsinki', 'full', 1.00, 51.00, 312, 0.570, 177.84, 'Pysäköinti työmaalla', 12.00, 240.84, NULL, 'unpaid', '2025-03-23 18:10:00', '2025-03-23 18:10:00');

UPDATE gbsapp_billingcaserow SET travel_exp_claim_id = 107, payroll_id = 107 WHERE id = 107;

UPDATE gbsapp_billingcaserow SET travel_exp_claim_id = 108, payroll_id = 108 WHERE id = 108;

UPDATE gbsapp_billingcaserow SET travel_exp_claim_id = 109, payroll_id = 109 WHERE id = 109;

UPDATE gbsapp_billingcaserow SET travel_exp_claim_id = 110, payroll_id = 110 WHERE id = 110;

UPDATE gbsapp_billingcaserow SET travel_exp_claim_id = 111, payroll_id = 111 WHERE id = 111;

UPDATE gbsapp_billingcaserow SET travel_exp_claim_id = 112, payroll_id = 112 WHERE id = 112;

UPDATE gbsapp_billingcaserow SET travel_exp_claim_id = 113, payroll_id = 113 WHERE id = 113;

UPDATE gbsapp_billingcaserow SET travel_exp_claim_id = 114, payroll_id = 114 WHERE id = 114;

UPDATE gbsapp_billingcaserow SET travel_exp_claim_id = 115, payroll_id = 115 WHERE id = 115;

UPDATE gbsapp_billingcaserow SET travel_exp_claim_id = 116, payroll_id = 116 WHERE id = 116;

UPDATE gbsapp_billingcaserow SET travel_exp_claim_id = 117, payroll_id = 117 WHERE id = 117;

UPDATE gbsapp_billingcaserow SET travel_exp_claim_id = 118, payroll_id = 118 WHERE id = 118;

UPDATE gbsapp_billingcaserow SET travel_exp_claim_id = 119, payroll_id = 119 WHERE id = 119;

UPDATE gbsapp_billingcaserow SET travel_exp_claim_id = 120, payroll_id = 120 WHERE id = 120;

UPDATE gbsapp_billingcaserow SET travel_exp_claim_id = 121, payroll_id = 121 WHERE id = 121;

UPDATE gbsapp_billingcaserow SET travel_exp_claim_id = 122, payroll_id = 122 WHERE id = 122;

INSERT INTO gbsapp_invoice (
    id, billing_case_id_id, billing_cust_id_id, invoice_num, invoice_date,
    due_date, invoice_status, description, salary_sum, travel_exp_sum,
    other_claims_sum, amount_vat_0, vat_percent, vat_sum, total_amount,
    reference, bank_account, paid_amount, penalty_interest, payment_date,
    payment_state, created, updated
) VALUES
(107, 107, 108, 'LASKU-2025-107', '2025-03-15', '2025-03-29', 'sent', 'Sähkökeskuksen huolto ja tarkastus / Pohjolan Rakennus Oy', 357.00, 138.60, 12.00, 507.60, 'ALV 25.5%',1, 129.44, 637.04, '2025000107', 'FI2112345600000001', 637.04, 0.00, '2025-03-27', 'paid', '2025-03-15 14:00:00', '2025-03-15 14:00:00'),
(108, 108, 109, 'LASKU-2025-108', '2025-03-16', '2025-03-30', 'sent', 'Varastovalaistuksen asennus / Arktis Logistiikka Oy', 351.00, 231.94, 37.00, 619.94, 'ALV 25.5%',1, 158.08, 778.02, '2025000108', 'FI2212345600000001', NULL, 0.00, NULL, 'unpaid', '2025-03-16 14:00:00', '2025-03-16 14:00:00'),
(109, 109, 110, 'LASKU-2025-109', '2025-03-17', '2025-03-31', 'sent', 'Kaapelointityö tuotantolinjalla / Savon Sähköhuolto Oy', 336.00, 152.28, 12.00, 500.28, 'ALV 25.5%',1, 127.57, 627.85, '2025000109', 'FI2312345600000001', 0.00, 12.45, NULL, 'debt_collection', '2025-03-17 14:00:00', '2025-03-17 14:00:00'),
(110, 110, 111, 'LASKU-2025-110', '2025-03-18', '2025-04-01', 'sent', 'Kiinteistötekniikan vikakorjaus / Turun Kiinteistöapu Oy', 357.00, 186.12, 12.00, 555.12, 'ALV 25.5%',1, 141.56, 696.68, '2025000110', 'FI2412345600000001', 696.68, 0.00, '2025-03-30', 'paid', '2025-03-18 14:00:00', '2025-03-18 14:00:00'),
(111, 111, 112, 'LASKU-2025-111', '2025-03-19', '2025-04-02', 'sent', 'Sähkökeskuksen huolto ja tarkastus / Oulun Teollisuuspalvelu Oy', 351.00, 198.46, 37.00, 586.46, 'ALV 25.5%',1, 149.55, 736.01, '2025000111', 'FI2512345600000001', 736.01, 0.00, '2025-03-31', 'paid', '2025-03-19 14:00:00', '2025-03-19 14:00:00'),
(112, 112, 113, 'LASKU-2025-112', '2025-03-20', '2025-04-03', 'sent', 'Varastovalaistuksen asennus / Järvimaan Infra Oy', 336.00, 199.80, 12.00, 547.80, 'ALV 25.5%',1, 139.69, 687.49, '2025000112', 'FI2612345600000001', NULL, 0.00, NULL, 'unpaid', '2025-03-20 14:00:00', '2025-03-20 14:00:00'),
(113, 113, 114, 'LASKU-2025-113', '2025-03-21', '2025-04-04', 'sent', 'Kaapelointityö tuotantolinjalla / Keski-Suomen Koneasennus Oy', 357.00, 179.64, 12.00, 548.64, 'ALV 25.5%',1, 139.90, 688.54, '2025000113', 'FI2712345600000001', 0.00, 12.45, NULL, 'debt_collection', '2025-03-21 14:00:00', '2025-03-21 14:00:00'),
(114, 114, 115, 'LASKU-2025-114', '2025-03-22', '2025-04-05', 'sent', 'Kiinteistötekniikan vikakorjaus / Lapin Huoltorengas Oy', 351.00, 272.98, 37.00, 660.98, 'ALV 25.5%',1, 168.55, 829.53, '2025000114', 'FI2812345600000001', 829.53, 0.00, '2025-04-03', 'paid', '2025-03-22 14:00:00', '2025-03-22 14:00:00'),
(115, 115, 116, 'LASKU-2025-115', '2025-03-23', '2025-04-06', 'sent', 'Sähkökeskuksen huolto ja tarkastus / Saimaan LVI-Palvelu Oy', 336.00, 193.32, 12.00, 541.32, 'ALV 25.5%',1, 138.04, 679.36, '2025000115', 'FI2912345600000001', 679.36, 0.00, '2025-04-04', 'paid', '2025-03-23 14:00:00', '2025-03-23 14:00:00'),
(116, 116, 117, 'LASKU-2025-116', '2025-03-24', '2025-04-07', 'sent', 'Varastovalaistuksen asennus / Uudenmaan Sähkötiimi Oy', 357.00, 227.16, 12.00, 596.16, 'ALV 25.5%',1, 152.02, 748.18, '2025000116', 'FI3012345600000001', NULL, 0.00, NULL, 'unpaid', '2025-03-24 14:00:00', '2025-03-24 14:00:00'),
(117, 117, 118, 'LASKU-2025-117', '2025-03-25', '2025-04-08', 'sent', 'Kaapelointityö tuotantolinjalla / Pohjolan Rakennus Oy', 351.00, 239.50, 37.00, 627.50, 'ALV 25.5%',1, 160.01, 787.51, '2025000117', 'FI3112345600000001', 0.00, 12.45, NULL, 'debt_collection', '2025-03-25 14:00:00', '2025-03-25 14:00:00'),
(118, 118, 119, 'LASKU-2025-118', '2025-03-26', '2025-04-09', 'sent', 'Kiinteistötekniikan vikakorjaus / Arktis Logistiikka Oy', 336.00, 240.84, 12.00, 588.84, 'ALV 25.5%',1, 150.15, 738.99, '2025000118', 'FI3212345600000001', 738.99, 0.00, '2025-04-07', 'paid', '2025-03-26 14:00:00', '2025-03-26 14:00:00');

INSERT INTO gbsapp_documents (
    id, doc_type, doc_date, user_id_id, contract_id_id, invoice_id_id,
    payroll_id_id, docname, filepath, created, updated
) VALUES
(107, 'tax card', '2025-02-01', 107, NULL, NULL, NULL, 'verokortti_jari_koskinen_2025.pdf', '/docs/taxcards/verokortti_jari_koskinen_2025.pdf', '2025-02-01 09:20:00', '2025-02-01 09:20:00'),
(108, 'tax card', '2025-02-01', 108, NULL, NULL, NULL, 'verokortti_anne_heikkinen_2025.pdf', '/docs/taxcards/verokortti_anne_heikkinen_2025.pdf', '2025-02-01 09:20:00', '2025-02-01 09:20:00'),
(109, 'tax card', '2025-02-01', 109, NULL, NULL, NULL, 'verokortti_timo_niemi_2025.pdf', '/docs/taxcards/verokortti_timo_niemi_2025.pdf', '2025-02-01 09:20:00', '2025-02-01 09:20:00'),
(110, 'tax card', '2025-02-01', 110, NULL, NULL, NULL, 'verokortti_kaisa_salmi_2025.pdf', '/docs/taxcards/verokortti_kaisa_salmi_2025.pdf', '2025-02-01 09:20:00', '2025-02-01 09:20:00'),
(111, 'tax card', '2025-02-01', 111, NULL, NULL, NULL, 'verokortti_olli_rantanen_2025.pdf', '/docs/taxcards/verokortti_olli_rantanen_2025.pdf', '2025-02-01 09:20:00', '2025-02-01 09:20:00'),
(112, 'tax card', '2025-02-01', 112, NULL, NULL, NULL, 'verokortti_minna_lehto_2025.pdf', '/docs/taxcards/verokortti_minna_lehto_2025.pdf', '2025-02-01 09:20:00', '2025-02-01 09:20:00'),
(113, 'tax card', '2025-02-01', 113, NULL, NULL, NULL, 'verokortti_petri_aalto_2025.pdf', '/docs/taxcards/verokortti_petri_aalto_2025.pdf', '2025-02-01 09:20:00', '2025-02-01 09:20:00'),
(114, 'tax card', '2025-02-01', 114, NULL, NULL, NULL, 'verokortti_laura_hamalainen_2025.pdf', '/docs/taxcards/verokortti_laura_hamalainen_2025.pdf', '2025-02-01 09:20:00', '2025-02-01 09:20:00'),
(115, 'tax card', '2025-02-01', 115, NULL, NULL, NULL, 'verokortti_mikko_seppanen_2025.pdf', '/docs/taxcards/verokortti_mikko_seppanen_2025.pdf', '2025-02-01 09:20:00', '2025-02-01 09:20:00'),
(116, 'tax card', '2025-02-01', 116, NULL, NULL, NULL, 'verokortti_riikka_makinen_2025.pdf', '/docs/taxcards/verokortti_riikka_makinen_2025.pdf', '2025-02-01 09:20:00', '2025-02-01 09:20:00'),
(117, 'tax card', '2025-02-01', 117, NULL, NULL, NULL, 'verokortti_sami_laaksonen_2025.pdf', '/docs/taxcards/verokortti_sami_laaksonen_2025.pdf', '2025-02-01 09:20:00', '2025-02-01 09:20:00'),
(118, 'tax card', '2025-02-01', 118, NULL, NULL, NULL, 'verokortti_johanna_toivonen_2025.pdf', '/docs/taxcards/verokortti_johanna_toivonen_2025.pdf', '2025-02-01 09:20:00', '2025-02-01 09:20:00'),
(119, 'tax card', '2025-02-01', 119, NULL, NULL, NULL, 'verokortti_antti_jokinen_2025.pdf', '/docs/taxcards/verokortti_antti_jokinen_2025.pdf', '2025-02-01 09:20:00', '2025-02-01 09:20:00'),
(120, 'tax card', '2025-02-01', 120, NULL, NULL, NULL, 'verokortti_elina_saarinen_2025.pdf', '/docs/taxcards/verokortti_elina_saarinen_2025.pdf', '2025-02-01 09:20:00', '2025-02-01 09:20:00'),
(121, 'tax card', '2025-02-01', 121, NULL, NULL, NULL, 'verokortti_ville_kinnunen_2025.pdf', '/docs/taxcards/verokortti_ville_kinnunen_2025.pdf', '2025-02-01 09:20:00', '2025-02-01 09:20:00'),
(122, 'tax card', '2025-02-01', 122, NULL, NULL, NULL, 'verokortti_mari_peltonen_2025.pdf', '/docs/taxcards/verokortti_mari_peltonen_2025.pdf', '2025-02-01 09:20:00', '2025-02-01 09:20:00'),
(123, 'tax card', '2025-02-01', 123, NULL, NULL, NULL, 'verokortti_juha_hietala_2025.pdf', '/docs/taxcards/verokortti_juha_hietala_2025.pdf', '2025-02-01 09:20:00', '2025-02-01 09:20:00'),
(124, 'tax card', '2025-02-01', 124, NULL, NULL, NULL, 'verokortti_sanna_kuusela_2025.pdf', '/docs/taxcards/verokortti_sanna_kuusela_2025.pdf', '2025-02-01 09:20:00', '2025-02-01 09:20:00'),
(125, 'tax card', '2025-02-01', 125, NULL, NULL, NULL, 'verokortti_teemu_nurmi_2025.pdf', '/docs/taxcards/verokortti_teemu_nurmi_2025.pdf', '2025-02-01 09:20:00', '2025-02-01 09:20:00'),
(126, 'tax card', '2025-02-01', 126, NULL, NULL, NULL, 'verokortti_paula_karjalainen_2025.pdf', '/docs/taxcards/verokortti_paula_karjalainen_2025.pdf', '2025-02-01 09:20:00', '2025-02-01 09:20:00'),
(127, 'payroll', '2025-03-20', 107, NULL, NULL, 107, 'palkkalaskelma_03_2025_107.pdf', '/docs/payroll/palkkalaskelma_03_2025_107.pdf', '2025-03-15 12:00:00', '2025-03-15 12:00:00'),
(128, 'other appendix', '2025-03-20', 107, NULL, NULL, NULL, 'matkalasku_helsinki_107.pdf', '/docs/appendices/matkalasku_helsinki_107.pdf', '2025-03-12 18:10:00', '2025-03-12 18:10:00'),
(129, 'contract', '2025-03-05', 107, 107, NULL, NULL, 'sopimus_SOP-2025-107.pdf', '/docs/contracts/sopimus_SOP-2025-107.pdf', '2025-03-05 09:30:00', '2025-03-05 09:30:00'),
(130, 'accepted contract', '2025-03-11', 107, 107, NULL, NULL, 'hyvaksytty_sopimus_SOP-2025-107.pdf', '/docs/contracts/hyvaksytty_sopimus_SOP-2025-107.pdf', '2025-03-05 09:30:00', '2025-03-05 09:30:00'),
(131, 'invoice', '2025-03-15', 108, NULL, 107, NULL, 'lasku_LASKU-2025-107.pdf', '/docs/invoices/lasku_LASKU-2025-107.pdf', '2025-03-15 14:00:00', '2025-03-15 14:00:00'),
(132, 'payroll', '2025-03-21', 108, NULL, NULL, 108, 'palkkalaskelma_03_2025_108.pdf', '/docs/payroll/palkkalaskelma_03_2025_108.pdf', '2025-03-16 12:00:00', '2025-03-16 12:00:00'),
(133, 'other appendix', '2025-03-21', 108, NULL, NULL, NULL, 'matkalasku_tampere_108.pdf', '/docs/appendices/matkalasku_tampere_108.pdf', '2025-03-13 18:10:00', '2025-03-13 18:10:00'),
(134, 'payroll', '2025-03-21', 109, NULL, NULL, 109, 'palkkalaskelma_03_2025_109.pdf', '/docs/payroll/palkkalaskelma_03_2025_109.pdf', '2025-03-16 12:01:00', '2025-03-16 12:01:00'),
(135, 'other appendix', '2025-03-21', 109, NULL, NULL, NULL, 'matkalasku_tampere_109.pdf', '/docs/appendices/matkalasku_tampere_109.pdf', '2025-03-13 18:11:00', '2025-03-13 18:11:00'),
(136, 'contract', '2025-03-06', 108, 108, NULL, NULL, 'sopimus_SOP-2025-108.pdf', '/docs/contracts/sopimus_SOP-2025-108.pdf', '2025-03-06 09:30:00', '2025-03-06 09:30:00'),
(137, 'invoice', '2025-03-16', 109, NULL, 108, NULL, 'lasku_LASKU-2025-108.pdf', '/docs/invoices/lasku_LASKU-2025-108.pdf', '2025-03-16 14:00:00', '2025-03-16 14:00:00'),
(138, 'payroll', '2025-03-22', 109, NULL, NULL, 110, 'palkkalaskelma_03_2025_109.pdf', '/docs/payroll/palkkalaskelma_03_2025_109.pdf', '2025-03-17 12:00:00', '2025-03-17 12:00:00'),
(139, 'other appendix', '2025-03-22', 109, NULL, NULL, NULL, 'matkalasku_kuopio_110.pdf', '/docs/appendices/matkalasku_kuopio_110.pdf', '2025-03-14 18:10:00', '2025-03-14 18:10:00'),
(140, 'contract', '2025-03-07', 109, 109, NULL, NULL, 'sopimus_SOP-2025-109.pdf', '/docs/contracts/sopimus_SOP-2025-109.pdf', '2025-03-07 09:30:00', '2025-03-07 09:30:00'),
(141, 'accepted contract', '2025-03-13', 109, 109, NULL, NULL, 'hyvaksytty_sopimus_SOP-2025-109.pdf', '/docs/contracts/hyvaksytty_sopimus_SOP-2025-109.pdf', '2025-03-07 09:30:00', '2025-03-07 09:30:00'),
(142, 'invoice', '2025-03-17', 110, NULL, 109, NULL, 'lasku_LASKU-2025-109.pdf', '/docs/invoices/lasku_LASKU-2025-109.pdf', '2025-03-17 14:00:00', '2025-03-17 14:00:00'),
(143, 'payroll', '2025-03-23', 110, NULL, NULL, 111, 'palkkalaskelma_03_2025_110.pdf', '/docs/payroll/palkkalaskelma_03_2025_110.pdf', '2025-03-18 12:00:00', '2025-03-18 12:00:00'),
(144, 'other appendix', '2025-03-23', 110, NULL, NULL, NULL, 'matkalasku_turku_111.pdf', '/docs/appendices/matkalasku_turku_111.pdf', '2025-03-15 18:10:00', '2025-03-15 18:10:00'),
(145, 'contract', '2025-03-08', 110, 110, NULL, NULL, 'sopimus_SOP-2025-110.pdf', '/docs/contracts/sopimus_SOP-2025-110.pdf', '2025-03-08 09:30:00', '2025-03-08 09:30:00'),
(146, 'invoice', '2025-03-18', 111, NULL, 110, NULL, 'lasku_LASKU-2025-110.pdf', '/docs/invoices/lasku_LASKU-2025-110.pdf', '2025-03-18 14:00:00', '2025-03-18 14:00:00'),
(147, 'payroll', '2025-03-24', 111, NULL, NULL, 112, 'palkkalaskelma_03_2025_111.pdf', '/docs/payroll/palkkalaskelma_03_2025_111.pdf', '2025-03-19 12:00:00', '2025-03-19 12:00:00'),
(148, 'other appendix', '2025-03-24', 111, NULL, NULL, NULL, 'matkalasku_oulu_112.pdf', '/docs/appendices/matkalasku_oulu_112.pdf', '2025-03-16 18:10:00', '2025-03-16 18:10:00'),
(149, 'payroll', '2025-03-24', 112, NULL, NULL, 113, 'palkkalaskelma_03_2025_112.pdf', '/docs/payroll/palkkalaskelma_03_2025_112.pdf', '2025-03-19 12:01:00', '2025-03-19 12:01:00'),
(150, 'other appendix', '2025-03-24', 112, NULL, NULL, NULL, 'matkalasku_oulu_113.pdf', '/docs/appendices/matkalasku_oulu_113.pdf', '2025-03-16 18:11:00', '2025-03-16 18:11:00'),
(151, 'contract', '2025-03-09', 111, 111, NULL, NULL, 'sopimus_SOP-2025-111.pdf', '/docs/contracts/sopimus_SOP-2025-111.pdf', '2025-03-09 09:30:00', '2025-03-09 09:30:00'),
(152, 'accepted contract', '2025-03-15', 111, 111, NULL, NULL, 'hyvaksytty_sopimus_SOP-2025-111.pdf', '/docs/contracts/hyvaksytty_sopimus_SOP-2025-111.pdf', '2025-03-09 09:30:00', '2025-03-09 09:30:00'),
(153, 'invoice', '2025-03-19', 112, NULL, 111, NULL, 'lasku_LASKU-2025-111.pdf', '/docs/invoices/lasku_LASKU-2025-111.pdf', '2025-03-19 14:00:00', '2025-03-19 14:00:00'),
(154, 'payroll', '2025-03-25', 112, NULL, NULL, 114, 'palkkalaskelma_03_2025_112.pdf', '/docs/payroll/palkkalaskelma_03_2025_112.pdf', '2025-03-20 12:00:00', '2025-03-20 12:00:00'),
(155, 'other appendix', '2025-03-25', 112, NULL, NULL, NULL, 'matkalasku_joensuu_114.pdf', '/docs/appendices/matkalasku_joensuu_114.pdf', '2025-03-17 18:10:00', '2025-03-17 18:10:00'),
(156, 'contract', '2025-03-10', 112, 112, NULL, NULL, 'sopimus_SOP-2025-112.pdf', '/docs/contracts/sopimus_SOP-2025-112.pdf', '2025-03-10 09:30:00', '2025-03-10 09:30:00'),
(157, 'invoice', '2025-03-20', 113, NULL, 112, NULL, 'lasku_LASKU-2025-112.pdf', '/docs/invoices/lasku_LASKU-2025-112.pdf', '2025-03-20 14:00:00', '2025-03-20 14:00:00'),
(158, 'payroll', '2025-03-26', 113, NULL, NULL, 115, 'palkkalaskelma_03_2025_113.pdf', '/docs/payroll/palkkalaskelma_03_2025_113.pdf', '2025-03-21 12:00:00', '2025-03-21 12:00:00'),
(159, 'other appendix', '2025-03-26', 113, NULL, NULL, NULL, 'matkalasku_jyväskylä_115.pdf', '/docs/appendices/matkalasku_jyväskylä_115.pdf', '2025-03-18 18:10:00', '2025-03-18 18:10:00'),
(160, 'contract', '2025-03-11', 113, 113, NULL, NULL, 'sopimus_SOP-2025-113.pdf', '/docs/contracts/sopimus_SOP-2025-113.pdf', '2025-03-11 09:30:00', '2025-03-11 09:30:00'),
(161, 'accepted contract', '2025-03-17', 113, 113, NULL, NULL, 'hyvaksytty_sopimus_SOP-2025-113.pdf', '/docs/contracts/hyvaksytty_sopimus_SOP-2025-113.pdf', '2025-03-11 09:30:00', '2025-03-11 09:30:00'),
(162, 'invoice', '2025-03-21', 114, NULL, 113, NULL, 'lasku_LASKU-2025-113.pdf', '/docs/invoices/lasku_LASKU-2025-113.pdf', '2025-03-21 14:00:00', '2025-03-21 14:00:00'),
(163, 'payroll', '2025-03-27', 114, NULL, NULL, 116, 'palkkalaskelma_03_2025_114.pdf', '/docs/payroll/palkkalaskelma_03_2025_114.pdf', '2025-03-22 12:00:00', '2025-03-22 12:00:00'),
(164, 'other appendix', '2025-03-27', 114, NULL, NULL, NULL, 'matkalasku_rovaniemi_116.pdf', '/docs/appendices/matkalasku_rovaniemi_116.pdf', '2025-03-19 18:10:00', '2025-03-19 18:10:00'),
(165, 'payroll', '2025-03-27', 115, NULL, NULL, 117, 'palkkalaskelma_03_2025_115.pdf', '/docs/payroll/palkkalaskelma_03_2025_115.pdf', '2025-03-22 12:01:00', '2025-03-22 12:01:00'),
(166, 'other appendix', '2025-03-27', 115, NULL, NULL, NULL, 'matkalasku_rovaniemi_117.pdf', '/docs/appendices/matkalasku_rovaniemi_117.pdf', '2025-03-19 18:11:00', '2025-03-19 18:11:00'),
(167, 'contract', '2025-03-12', 114, 114, NULL, NULL, 'sopimus_SOP-2025-114.pdf', '/docs/contracts/sopimus_SOP-2025-114.pdf', '2025-03-12 09:30:00', '2025-03-12 09:30:00'),
(168, 'invoice', '2025-03-22', 115, NULL, 114, NULL, 'lasku_LASKU-2025-114.pdf', '/docs/invoices/lasku_LASKU-2025-114.pdf', '2025-03-22 14:00:00', '2025-03-22 14:00:00'),
(169, 'payroll', '2025-03-28', 115, NULL, NULL, 118, 'palkkalaskelma_03_2025_115.pdf', '/docs/payroll/palkkalaskelma_03_2025_115.pdf', '2025-03-23 12:00:00', '2025-03-23 12:00:00'),
(170, 'other appendix', '2025-03-28', 115, NULL, NULL, NULL, 'matkalasku_lappeenranta_118.pdf', '/docs/appendices/matkalasku_lappeenranta_118.pdf', '2025-03-20 18:10:00', '2025-03-20 18:10:00'),
(171, 'contract', '2025-03-13', 115, 115, NULL, NULL, 'sopimus_SOP-2025-115.pdf', '/docs/contracts/sopimus_SOP-2025-115.pdf', '2025-03-13 09:30:00', '2025-03-13 09:30:00'),
(172, 'accepted contract', '2025-03-19', 115, 115, NULL, NULL, 'hyvaksytty_sopimus_SOP-2025-115.pdf', '/docs/contracts/hyvaksytty_sopimus_SOP-2025-115.pdf', '2025-03-13 09:30:00', '2025-03-13 09:30:00'),
(173, 'invoice', '2025-03-23', 116, NULL, 115, NULL, 'lasku_LASKU-2025-115.pdf', '/docs/invoices/lasku_LASKU-2025-115.pdf', '2025-03-23 14:00:00', '2025-03-23 14:00:00'),
(174, 'payroll', '2025-03-29', 116, NULL, NULL, 119, 'palkkalaskelma_03_2025_116.pdf', '/docs/payroll/palkkalaskelma_03_2025_116.pdf', '2025-03-24 12:00:00', '2025-03-24 12:00:00'),
(175, 'other appendix', '2025-03-29', 116, NULL, NULL, NULL, 'matkalasku_vantaa_119.pdf', '/docs/appendices/matkalasku_vantaa_119.pdf', '2025-03-21 18:10:00', '2025-03-21 18:10:00'),
(176, 'contract', '2025-03-14', 116, 116, NULL, NULL, 'sopimus_SOP-2025-116.pdf', '/docs/contracts/sopimus_SOP-2025-116.pdf', '2025-03-14 09:30:00', '2025-03-14 09:30:00'),
(177, 'invoice', '2025-03-24', 117, NULL, 116, NULL, 'lasku_LASKU-2025-116.pdf', '/docs/invoices/lasku_LASKU-2025-116.pdf', '2025-03-24 14:00:00', '2025-03-24 14:00:00'),
(178, 'payroll', '2025-03-30', 117, NULL, NULL, 120, 'palkkalaskelma_03_2025_117.pdf', '/docs/payroll/palkkalaskelma_03_2025_117.pdf', '2025-03-25 12:00:00', '2025-03-25 12:00:00'),
(179, 'other appendix', '2025-03-30', 117, NULL, NULL, NULL, 'matkalasku_helsinki_120.pdf', '/docs/appendices/matkalasku_helsinki_120.pdf', '2025-03-22 18:10:00', '2025-03-22 18:10:00'),
(180, 'payroll', '2025-03-30', 118, NULL, NULL, 121, 'palkkalaskelma_03_2025_118.pdf', '/docs/payroll/palkkalaskelma_03_2025_118.pdf', '2025-03-25 12:01:00', '2025-03-25 12:01:00'),
(181, 'other appendix', '2025-03-30', 118, NULL, NULL, NULL, 'matkalasku_helsinki_121.pdf', '/docs/appendices/matkalasku_helsinki_121.pdf', '2025-03-22 18:11:00', '2025-03-22 18:11:00'),
(182, 'contract', '2025-03-15', 117, 117, NULL, NULL, 'sopimus_SOP-2025-117.pdf', '/docs/contracts/sopimus_SOP-2025-117.pdf', '2025-03-15 09:30:00', '2025-03-15 09:30:00'),
(183, 'accepted contract', '2025-03-21', 117, 117, NULL, NULL, 'hyvaksytty_sopimus_SOP-2025-117.pdf', '/docs/contracts/hyvaksytty_sopimus_SOP-2025-117.pdf', '2025-03-15 09:30:00', '2025-03-15 09:30:00'),
(184, 'invoice', '2025-03-25', 118, NULL, 117, NULL, 'lasku_LASKU-2025-117.pdf', '/docs/invoices/lasku_LASKU-2025-117.pdf', '2025-03-25 14:00:00', '2025-03-25 14:00:00'),
(185, 'payroll', '2025-03-31', 118, NULL, NULL, 122, 'palkkalaskelma_03_2025_118.pdf', '/docs/payroll/palkkalaskelma_03_2025_118.pdf', '2025-03-26 12:00:00', '2025-03-26 12:00:00'),
(186, 'other appendix', '2025-03-31', 118, NULL, NULL, NULL, 'matkalasku_tampere_122.pdf', '/docs/appendices/matkalasku_tampere_122.pdf', '2025-03-23 18:10:00', '2025-03-23 18:10:00'),
(187, 'contract', '2025-03-16', 118, 118, NULL, NULL, 'sopimus_SOP-2025-118.pdf', '/docs/contracts/sopimus_SOP-2025-118.pdf', '2025-03-16 09:30:00', '2025-03-16 09:30:00'),
(188, 'invoice', '2025-03-26', 119, NULL, 118, NULL, 'lasku_LASKU-2025-118.pdf', '/docs/invoices/lasku_LASKU-2025-118.pdf', '2025-03-26 14:00:00', '2025-03-26 14:00:00');

COMMIT;