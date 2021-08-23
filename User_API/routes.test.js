import axios from 'axios';
const BASE_URL = 'http://localhost:8000/';
import {describe, expect, it } from '@jest/globals'
import "core-js/stable";
import "regenerator-runtime/runtime";

describe('routes', () => {
  let token = '';
  let refreshtoken = '';

  it('should get the base url', async () => {
    const response = await axios.get(BASE_URL);
    expect(response.data).toBeTruthy();
    expect(response.data).toEqual('Hello from express and typescript');
  });

  it('creating user', async () => {
    let body = {
      "username":"test",
      "password":"test",
      "email":"pingouin"
    }
    const response = await axios.post(BASE_URL+'user', body);
    expect(response.data).toBeTruthy();
    console.log(response.data);
    expect(response.data.status).toEqual('ok');
  })

  it('login user', async () => {
    let body = {
      username:"test",
      password:"test",
    }
    const response = await axios.post(BASE_URL+'connect', body);
    expect(response.data).toBeTruthy();
    console.log(response.data);
    expect(response.data.status).toEqual('ok');
    token = response.data.token
    refreshtoken = response.data.refreshtoken
  })

  it('deleting user', async () => {
    let body = {
      username:"test",
      password:"test",
    }
    const response = await axios.delete(BASE_URL+'user', {
      data: body,
      headers: {
        "token":token,
        "refreshtoken":refreshtoken,
      }
    });
    expect(response.data).toBeTruthy();
    // expect(response.data.status).toEqual('ok');
    console.log(response.data);
  })
});
