/**
 * Google Apps Script - Web App Entry Point
 * โครงการผู้ช่วยระบบคำของบประมาณ (MIS Budget Chatbot)
 * มหาวิทยาลัยราชภัฏเลย
 */

function doGet(e) {
  return HtmlService.createHtmlOutputFromFile('Index')
    .setTitle('ผู้ช่วยระบบคำของบประมาณ — มหาวิทยาลัยราชภัฏเลย')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL)
    .addMetaTag('viewport', 'width=device-width, initial-scale=1.0');
}
