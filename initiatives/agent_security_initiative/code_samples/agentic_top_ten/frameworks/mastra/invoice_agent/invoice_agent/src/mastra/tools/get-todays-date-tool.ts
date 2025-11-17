import { createTool } from '@mastra/core/tools';
import { z } from 'zod';

export const getTodaysDateTool = createTool({
  id: 'get-todays-date',
  description: 'Get the current date in various formats',
  inputSchema: z.object({
    format: z.enum(['iso', 'full', 'date-only', 'timestamp', 'custom']).optional().describe('The format to return the date in'),
    customFormat: z.string().optional().describe('Custom format string (used when format is "custom")'),
  }),
  outputSchema: z.object({
    iso: z.string(),
    full: z.string(),
    dateOnly: z.string(),
    timestamp: z.number(),
    year: z.number(),
    month: z.number(),
    day: z.number(),
    dayOfWeek: z.number(),
    dayName: z.string(),
    monthName: z.string(),
    time: z.string(),
  }),
  execute: async ({ context }) => {
    return await getDateInfo(context.format, context.customFormat);
  },
});

const getDateInfo = async (format, customFormat) => {
  const today = new Date();

  const dayNames = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
  const monthNames = ['January', 'February', 'March', 'April', 'May', 'June',
                      'July', 'August', 'September', 'October', 'November', 'December'];

  const year = today.getFullYear();
  const month = today.getMonth() + 1;
  const day = today.getDate();
  const dayOfWeek = today.getDay();
  const hours = today.getHours();
  const minutes = today.getMinutes();
  const seconds = today.getSeconds();

  const dateInfo = {
    iso: today.toISOString(),
    full: today.toString(),
    dateOnly: `${year}-${String(month).padStart(2, '0')}-${String(day).padStart(2, '0')}`,
    timestamp: today.getTime(),
    year: year,
    month: month,
    day: day,
    dayOfWeek: dayOfWeek,
    dayName: dayNames[dayOfWeek],
    monthName: monthNames[month - 1],
    time: `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`,
  };

  if (format && format !== 'custom') {
    switch(format) {
      case 'iso':
        return { ...dateInfo, formatted: dateInfo.iso };
      case 'full':
        return { ...dateInfo, formatted: dateInfo.full };
      case 'date-only':
        return { ...dateInfo, formatted: dateInfo.dateOnly };
      case 'timestamp':
        return { ...dateInfo, formatted: dateInfo.timestamp };
      default:
        return dateInfo;
    }
  }

  if (format === 'custom' && customFormat) {
    let formatted = customFormat;
    formatted = formatted.replace('YYYY', year);
    formatted = formatted.replace('MM', String(month).padStart(2, '0'));
    formatted = formatted.replace('DD', String(day).padStart(2, '0'));
    formatted = formatted.replace('HH', String(hours).padStart(2, '0'));
    formatted = formatted.replace('mm', String(minutes).padStart(2, '0'));
    formatted = formatted.replace('ss', String(seconds).padStart(2, '0'));
    formatted = formatted.replace('DAY', dayNames[dayOfWeek]);
    formatted = formatted.replace('MONTH', monthNames[month - 1]);

    return { ...dateInfo, formatted };
  }

  return dateInfo;
};