function add(nums) {
    if (!nums) return 0;

    let delimiters = [",", "\n"]; // default delimiters: comma and newline
    // check if a custom delimiter is specified
    if (nums.startsWith("//")) {
        let parts = nums.split("\n"); // split the numbers separately
        let customDelimiters = parts[0].slice(2); // extract delimiters
        let delimiterMatches = customDelimiters.match(/\[([^\]]+)\]/g); // find multiple delimiters in square brackets

        // extract multiple delimiters if matches, else single-character delimiter
        if (delimiterMatches) {
            delimiters = delimiterMatches.map(d => d.slice(1, -1));
        } else {
            delimiters = [customDelimiters];
        }

        // remove delimiter header and keep the number part
        nums = parts.slice(1).join("\n");
    }

    // split the numbers using detected delimiters and then convert the string to individual numbers
    let regex = new RegExp(delimiters.map(d => d.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")).join("|"));
    let numList = nums.split(regex).map(Number);

    // check for negative numbers and throw custom error
    let negatives = numList.filter(n => n < 0);
    if (negatives.length) {
        throw new Error(`negative numbers not allowed: ${negatives.join(",")}`);
    }

    // return the sum of the numbers after ignoring numbers > 1000 (converted from string after extracting delimiters)
    return numList.filter(n => n < 1000).reduce((sum, n) => sum + n, 0);
}

module.exports = add;