export const postJson = (url, data) => {
  // Returns a promise with JS data
  const headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  };
  const req = {
    headers,
    method: 'POST',
    body: JSON.stringify(data),
  };
  return fetch(url, req).then(res => res.json());
}

export const shuffleArr = a => {
  let b = Array.from(a);
  for (let i = b.length; i; i--) {
    let j = Math.floor(Math.random() * i);
    [b[i - 1], b[j]] = [b[j], b[i - 1]];
  }
  return b;
}
