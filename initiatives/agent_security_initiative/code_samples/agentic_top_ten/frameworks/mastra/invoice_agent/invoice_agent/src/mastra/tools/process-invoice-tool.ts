import { createTool } from '@mastra/core/tools';
import { z } from 'zod';

export const processInvoiceTool = createTool({
  id: 'process-invoice',
  description: 'Process an invoice from a JSON string with amount, category, submitter, and dueDate.',
  inputSchema: z.object({
    invoiceJson: z.string().describe('A JSON string with keys: amount (integer), category (string), submitter (string), dueDate (date in YYYY-MM-DD format)'),
  }),
  outputSchema: z.object({
    amount: z.number(),
    category: z.string(),
    submitter: z.string(),
    dueDate: z.string(),
  }),
  execute: async ({ context }) => {
    return await processInvoice(context.invoiceJson);
  },
});

const invoiceSchema = z.object({
  amount: z.number(),
  category: z.string(),
  submitter: z.string(),
  dueDate: z.string().refine(
    (date) => /^\d{4}-\d{2}-\d{2}$/.test(date),
    { message: 'dueDate must be in YYYY-MM-DD format' }
  ),
});

const processInvoice = async (invoiceJson: string) => {
  let parsed;
  try {
    parsed = JSON.parse(invoiceJson);
  } catch (e) {
    throw new Error('Invalid JSON string');
  }
  const result = invoiceSchema.safeParse(parsed);
  if (!result.success) {
    throw new Error('Invalid invoice data: ' + JSON.stringify(result.error.issues));
  }

  return result.data;
};
