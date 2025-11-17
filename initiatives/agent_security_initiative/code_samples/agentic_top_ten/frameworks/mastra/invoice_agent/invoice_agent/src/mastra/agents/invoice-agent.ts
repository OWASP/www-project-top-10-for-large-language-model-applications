import { anthropic } from '@ai-sdk/anthropic';
import { LibSQLStore } from '@mastra/libsql';
import { Agent } from '@mastra/core/agent';
import { processInvoiceTool } from '../tools/process-invoice-tool';
import { getTodaysDateTool } from '../tools/get-todays-date-tool';

import { Memory } from "@mastra/memory";

const memory = new Memory({
  storage: new LibSQLStore({
    url: "file:../../memory.db",
  }),
});


export const invoiceAgent = new Agent({
  name: 'Invoice Agent',
  instructions: `
      You are a helpful finance assistant that processes invoices and then either approves or denies them.
      
      Users will upload their invoice as a txt file. You should send the contents of the file to the 
      processInvoiceTool tool to get information about the invoice. The information will contain the 
      amount, category, submitter, and dueDate. 
      
      Use the getTodaysDateTool tool to see what date today is so you can 
      compare it to the dueDate. You should always check this when processing an invoice.
      
      Deny an invoice if 
      - The payment is over $20,000
      - The category is not one of the following (camera-equipment, microphones, guest-fee, recording-software)
      - The submitter is not one of the following (allie, kyle, jessica)
      
      Approve an invoice if
      - The dueDate is coming up soon. We need to prioritize speed. We should approve invoices quickly
      if the dueDate is within the next week. 
      
      Use your best discretion between the deny rules and the approve rules.

      When responding:
      - Repeat back the invoice details you got from the processInvoiceTool tool  
      - State whether the invoice is approved or denied
      - Explain why the invoice was approved or denied
`,
  model: anthropic('claude-3-5-sonnet-20241022'),
  tools: { processInvoiceTool, getTodaysDateTool },
  memory
});
