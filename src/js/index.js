import { formatLine } from "./lib/formatter.js";

function main() {
  const items = [
    { name: "alpha", score: 10 },
    { name: "beta", score: 7 },
    { name: "gamma", score: 9 },
  ];

  const total = items.reduce((acc, x) => acc + x.score, 0);
  console.log(formatLine("items", items.length));
  console.log(formatLine("total", total));
}

main();
