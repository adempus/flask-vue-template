// exports an object containing keys to respective endpoint string values on backend

const root = 'http://localhost:5000';
// const root = 'http://192.168.1.158:5000';
const endpoints = {
  root: root,
  test: `${root}/test-route`,
  auth: `${root}/authenticate`,
  signUp: `${root}/sign-up`,
  signIn: `${root}/sign-in`,
  getEntries: `${root}/get-user-entries`,
  postEntry: `${root}/post-new-entry`,
  deleteEntry: `${root}/delete-user-entry`,
};
Object.freeze(endpoints);

export default endpoints;
