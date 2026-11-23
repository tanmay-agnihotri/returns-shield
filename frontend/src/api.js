import axios from 'axios'
import { API_BASE_URL } from './config'

const api = axios.create({ baseURL: API_BASE_URL })

export const getStats = () => api.get('/returns/stats')
export const getAllReturns = () => api.get('/returns/all')
export const makeDecision = (id, decision) =>
  api.patch(`/returns/${id}/decide?decision=${decision}&notes=`)
export const analyzeReturn = (formData) =>
  api.post('/returns/analyze', formData)