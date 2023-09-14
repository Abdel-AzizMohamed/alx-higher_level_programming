#!/usr/bin/node
function factorial (fact) {
  if (fact === 1 || !fact) {
    return (1);
  }

  return (factorial(fact - 1) * fact);
}

console.log(factorial(Number(process.argv[2])));
