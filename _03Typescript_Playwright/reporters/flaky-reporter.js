class FlakyReporter {
    onTestEnd(test, result) {
      if (result.status === 'passed' && result.retry) {
        console.log(`🟡 Flaky Test Passed after ${result.retry} retries: ${test.title}`);
        test.annotations.push({ type: 'flaky', description: `Flaky after ${result.retry} retries` });
      }
    }
  }
  
  module.exports = FlakyReporter;
  