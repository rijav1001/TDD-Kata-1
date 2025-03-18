const add = require("./stringCalculator");

test("empty string returns zero", () => {
    expect(add("")).toBe(0);
});