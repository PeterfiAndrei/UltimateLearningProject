module.exports = [
  {
    ignores: ["node_modules", "dist","_04Python_Playwright"],
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
