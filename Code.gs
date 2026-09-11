/**
 * Google Apps Script - Web App Entry Point & Cloud Sync
 * โครงการผู้ช่วยระบบคำของบประมาณ (MIS Budget Chatbot)
 * มหาวิทยาลัยราชภัฏเลย
 */

// 1. ส่งหน้าเว็บแชทบอทให้ผู้ใช้งาน
function doGet(e) {
  return HtmlService.createHtmlOutputFromFile('Index')
    .setTitle('ผู้ช่วยระบบคำของบประมาณ — มหาวิทยาลัยราชภัฏเลย')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL)
    .addMetaTag('viewport', 'width=device-width, initial-scale=1.0');
}

// 2. รับข้อมูลประวัติคำถามจากผู้ใช้งานเพื่อบันทึกลง Google Sheet แบบ Real-time
function doPost(e) {
  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = ss ? ss.getActiveSheet() : null;
    
    if (!sheet) {
      return ContentService.createTextOutput(JSON.stringify({
        result: 'error',
        message: 'No active spreadsheet found'
      })).setMimeType(ContentService.MimeType.JSON);
    }

    var data = JSON.parse(e.postData.contents);
    var timestamp = new Date();
    
    // บันทึกแถวข้อมูล: [วันเวลา, คำถามผู้ใช้, สถานะการตอบ, หน้าคู่มืออ้างอิง, ขอบเขตบทบาท]
    sheet.appendRow([
      timestamp,
      data.query || '',
      data.status || '',
      data.page || '-',
      data.role || ''
    ]);

    return ContentService.createTextOutput(JSON.stringify({
      result: 'success',
      timestamp: timestamp
    })).setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({
      result: 'error',
      message: err.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}
