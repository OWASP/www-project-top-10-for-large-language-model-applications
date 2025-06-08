---
pdf_options:
  format: letter 
  margin: 0mm 0mm 20mm 0mm
  printBackground: true
  headerTemplate: |-
    <style>
      @media print {
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
      }
    </style>
  footerTemplate: |-
    <style>
      footer {
        margin: 0;
        margin-left: 30px;
        font-family: system-ui;
        text-align: center;
        padding: 10px;
        font-size: 12px;
        position: relative;
        width: 90%;
        height: 25px;
      }
      .left-text {
        position: absolute;
        top: 10px;
        left: 10px;
        bottom: 10px;
      }
      .right-text {
        position: absolute;
        top: 10px;
        right: 10px;
        bottom: 10px;
      }
    </style>
    <footer>
      <div class="left-text">
        <span>genai.owasp.org</span>
      </div>
    </footer>
---
