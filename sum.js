const seedrandom = require('seedrandom');

function generate(seed, rows, cols) {
  const random = seedrandom(seed);
  return Array.from({ length: rows }, () => Array.from({ length: cols }, () => Math.round(random() * 1000)));
}

let total_sum = 0;
for (let i = 1; i <= 10; i++) {
  const seed = i.toString();
  const tableData = generate(seed, 50, 10);
  for (let r = 0; r < 50; r++) {
    for (let c = 0; c < 10; c++) {
      total_sum += tableData[r][c];
    }
  }
}

console.log(total_sum);
