const fibonacciSequenceGenerator = (start, end) => {
  const fibList = [0, 1];
  for (let number = start; number <= end; number++) {
    fibList.push(fibList[fibList.length - 1] + fibList[fibList.length - 2]);
  }
  return fibList;
};

const fibList = fibonacciSequenceGenerator(1, 22);
console.log();
console.log(
  `The sequence consisting of the ${fibList.length} fibonacci numbers is:\n\n`,
  fibList
);
