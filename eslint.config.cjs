module.exports = [
  {
    ignores: ["node_modules", "dist","_04Python_Playwright","_03Typescript_Playwright/allure-report","_03Typescript_Playwright/allure-results"],
  },
  {
    languageOptions: {
      ecmaVersion: "latest",
      sourceType: "module",
    },
    plugins: {
      "@typescript-eslint": require("@typescript-eslint/eslint-plugin"),
    },
    rules: {
      "no-unused-vars": "warn",
      "no-console": "off",
    },
  },
];
