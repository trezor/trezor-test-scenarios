# Template Scenario

To allow import into [testpad](https://satoshilabs.ontestpad.com/) we need to stick to a certain format.

## Suite: Single Backup With Recovery Check

```
Firmware: latest
```

1. Wipe Device (via trezorctl wipe-device).
  ➡️ Device is reset to factory defaults and all private data is removed.
2. Launch Suite.
  ➡️ Suite is launched correctly and a Welcome splash screen is displayed.
3. Select the Let’s begin! button to initiate onboarding.
  ➡️ Fresh device flow is started, modal displays option to create a new wallet and to restore a wallet.
4. Select Create a new wallet option and select arbitrary options until Backup type selection is reached.
  ➡️ Backup type selection screen with options Single Seed and Shamir backup is displayed.
5. Select Single seed option and confirm.
  ➡️ action happened correctly
6. Select Backup your wallet, write down seed words and finish the process.
  ➡️ action happened correctly
7. Navigate to the Accounts section in the upper menu tab, select an arbitrary account and write down a BTC receive address.
  ➡️ action happened correctly
8. Repeat items 1 to 3. 
  ➡️ action happened correctly
9. Choose Recover wallet and click through.
  ➡️ action happened correctly
10. Confirm on Trezor and enter the words written down in step 7.
  ➡️ action happened correctly
11. Go through the recovery process and skip the rest of onboarding.
  ➡️ action happened correctly
12. Go to accounts and get a BTC address, confirm it equals the address in step 9.
  ➡️ action happened correctly
