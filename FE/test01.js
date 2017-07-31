// 实现一个函数输入123456789，输出123，456，789
// 
function toThousandslsFilter(num) {
  return (+num || 0).toString()
    .replace(/^\-?\d+/g, function (m) {
      return m.replace(/(?=(?!\b)(\d{3})+$)/g, ',');
    });
}
let a=toThousandslsFilter(123456789); // 123,456,789
console.log(a)