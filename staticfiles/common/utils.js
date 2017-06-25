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
