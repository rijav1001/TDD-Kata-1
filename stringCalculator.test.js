const add = require("./stringCalculator");

test("empty string returns zero", () => {
    expect(add("")).toBe(0);
});

test("newline delimiter", () => {
    expect(add("1\n2,3")).toBe(6);
});

test("custom delimiter", () => {
    expect(add("//;\n1;2")).toBe(3);
});

test("multiple delimiters", () => {
    expect(add("//[*][%]\n1*2%3")).toBe(6);
});

test("multiple delimiters with different lengths", () => {
    expect(add("//[**][%%]\n1**2%%3")).toBe(6);
});

test("single number", () => {
    expect(add("1")).toBe(1);
    expect(add("5")).toBe(5);
});

test("two numbers", () => {
    expect(add("1,2")).toBe(3);
});

test("multiple numbers", () => {
    expect(add("1,2,3")).toBe(6);
    expect(add("4,5,6,7")).toBe(22);
});

test("ignore larger numbers", () => {
    expect(add("2,1001")).toBe(2);
});

test("negative numbers not allowed", () => {
    expect(() => add("1,-2,3,-3")).toThrow("negative numbers not allowed: -2,-3");
});