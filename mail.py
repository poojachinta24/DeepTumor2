import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(number, mail, real_name, gender, age, status, length, width, area, location, decription, wtd, wtc, result):
    # Email account credentials
  wtd = " ".join(wtd)
  wtc = " ".join(wtc)
    
  html_template = """
  <!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
  <html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="x-apple-disable-message-reformatting">
    <!--[if !mso]><!--><meta http-equiv="X-UA-Compatible" content="IE=edge"><!--<![endif]-->

  <!--[if !mso]><!--><link href="https://fonts.googleapis.com/css?family=Raleway:400,700&display=swap" rel="stylesheet" type="text/css"><link href="https://fonts.googleapis.com/css2?family=Epilogue:wght@500&display=swap" rel="stylesheet" type="text/css"><!--<![endif]-->
  <style type="text/css">
  @media only screen and (min-width: 620px) {{
    .u-row {{
      width: 600px !important;
    }}
    .u-row .u-col {{
      vertical-align: top;
    }}

    .u-row .u-col-33p33 {{
      width: 199.98px !important;
    }}

    .u-row .u-col-37p74 {{
      width: 226.44px !important;
    }}

    .u-row .u-col-62p26 {{
      width: 373.56px !important;
    }}

    .u-row .u-col-66p67 {{
      width: 400.02px !important;
    }}

    .u-row .u-col-100 {{
      width: 600px !important;
    }}

  }}

  @media (max-width: 620px) {{
    .u-row-container {{
      max-width: 100% !important;
      padding-left: 0px !important;
      padding-right: 0px !important;
    }}
    .u-row .u-col {{
      min-width: 320px !important;
      max-width: 100% !important;
      display: block !important;
    }}
    .u-row {{
      width: 100% !important;
    }}
    .u-col {{
      width: 100% !important;
    }}
    .u-col > div {{
      margin: 0 auto;
    }}
  }}
  body {{
    margin: 0;
    padding: 0;
  }}

  table,
  tr,
  td {{
    vertical-align: top;
    border-collapse: collapse;
  }}

  p {{
    margin: 0;
  }}

  .ie-container table,
  .mso-container table {{
    table-layout: fixed;
  }}

  * {{
    line-height: inherit;
  }}

  a[x-apple-data-detectors='true'] {{
    color: inherit !important;
    text-decoration: none !important;
  }}

  table, td {{ color: #000000; }} 
  #u_body a {{ color: #0000ee; 
    text-decoration: underline; }} 
    
    #u_content_text_10 a {{ color: #f1c40f; }} 
    @media (max-width: 480px) 
    {{ #u_column_3 .v-col-border {{ border-top: 0px solid transparent !important;border-left: 0px solid transparent !important;border-right: 0px solid transparent !important;border-bottom: 0px solid transparent !important; }} 
    #u_content_heading_1 .v-container-padding-padding {{ padding: 20px 10px 0px !important; }} 
    #u_content_text_1 .v-container-padding-padding {{ padding: 10px 10px 0px !important; }} 
    #u_content_text_12 .v-container-padding-padding {{ padding: 10px 10px 0px !important; }} 
    #u_content_text_13 .v-container-padding-padding {{ padding: 10px 10px 0px !important; }} 
    #u_content_heading_2 .v-container-padding-padding {{ padding: 10px 10px 0px !important; }} 
    #u_content_heading_2 .v-font-size {{ font-size: 42px !important; }} 
    #u_content_heading_2 .v-line-height {{ line-height: 120% !important; }} 
    #u_content_heading_8 .v-font-size {{ font-size: 20px !important; }} 
    #u_content_text_2 .v-container-padding-padding {{ padding: 0px 10px !important; }} 
    #u_content_button_2 .v-size-width {{ width: 65% !important; }} 
    #u_content_heading_9 .v-container-padding-padding {{ padding: 40px 10px 10px !important; }} 
    #u_content_heading_9 .v-text-align {{ text-align: center !important; }} 
    #u_content_text_10 .v-container-padding-padding {{ padding: 10px 10px 0px !important; }} 
    #u_content_text_10 .v-text-align {{ text-align: center !important; }} 
    #u_content_social_1 .v-container-padding-padding {{ padding: 30px 0px 20px 75px !important; }} 
    #u_content_text_11 .v-container-padding-padding {{ padding: 20px 0px 10px !important; }} 
    #u_content_text_11 .v-font-size {{ font-size: 13px !important; }} 
    #u_content_text_11 .v-text-align {{ text-align: center !important; }} 
    #u_content_image_4 .v-container-padding-padding {{ padding: 10px 0px 20px !important; }} 
    #u_content_image_4 .v-src-width {{ width: auto !important; }} 
    #u_content_image_4 .v-src-max-width {{ max-width: 51% !important; }} 
    #u_content_image_4 .v-text-align {{ text-align: center !important; }} 
  }}

    .container {{
        text-align: center;
        animation: fadeIn 2s ease-in-out;
    }}

    .container h1 {{
        font-size: 3rem;
        color: #baff6674;
        margin: 0;
        animation: slideIn 3s ease-in-out infinite alternate;
    }}

    .container h2 {{
        font-size: 1.5rem;
        color: #baff6658;
        margin: 10px 0 0;
        animation: fadeIn 5s ease-in-out infinite alternate;
        padding-bottom: 20px;
    }}

    @keyframes slideIn {{
        from {{
            transform: translateX(-50px);
            opacity: 0;
        }}
        to {{
            transform: translateX(0);
            opacity: 1;
        }}
    }}

    @keyframes fadeIn {{
        0% {{
            opacity: 0;
        }}
        100% {{
            opacity: 1;
        }}
    }}
  </style>
  </head>

  <body class="clean-body u_body" style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%;background-color: #ecf0f1;color: #000000">
    <table id="u_body" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #ecf0f1;width:100%" cellpadding="0" cellspacing="0">
    <tbody>
    <tr style="vertical-align: top">
      <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
      
    
    
  <div class="u-row-container" style="padding: 0px;background-color: transparent">
    <div class="u-row" style="margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
      <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
        
  <div class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
    <div style="height: 100%;width: 100% !important;">
    <!--[if (!mso)&(!IE)]><!--><div class="v-col-border" style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
    
  <table style="font-family:'Raleway',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
      <tr>
        <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:0px;font-family:'Raleway',sans-serif;" align="left">
          
  <table width="100%" cellpadding="0" cellspacing="0" border="0">
    <tr>
      <td class="v-text-align" style="padding-right: 0px;padding-left: 0px;" align="center">
            <a href="https://postimg.cc/rdZgg70L" target="_blank"><img src="https://i.postimg.cc/rdZgg70L/image-5.png" alt="image-5" border="0" align="center"title="image" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 100%;max-width: 600px;" width="600" class="v-src-width v-src-max-width"/></a>
      </td>
    </tr>
  </table>

        </td>
      </tr>
    </tbody>
  </table>

    <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
    </div>
  </div>
      </div>
    </div>
    </div>
    

  
  <div class="u-row-container" style="padding: 0px;background-color: transparent">
    <div class="u-row" style="margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
      <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: transparent;"><![endif]-->
        
  <!--[if (mso)|(IE)]><td align="center" width="198" class="v-col-border" style="background-color: #1c1c1c;width: 198px;padding: 0px;border-top: 1px solid #777777;border-left: 1px solid #777777;border-right: 1px solid #777777;border-bottom: 1px solid #777777;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;" valign="top"><![endif]-->
  <div id="u_column_3" class="u-col u-col-33p33" style="max-width: 320px;min-width: 200px;display: table-cell;vertical-align: top;">
    <div style="background-color: #1c1c1c;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
    <!--[if (!mso)&(!IE)]><!--><div class="v-col-border" style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 1px solid #777777;border-left: 1px solid #777777;border-right: 1px solid #777777;border-bottom: 1px solid #777777;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;"><!--<![endif]-->
    
  <table id="u_content_heading_1" style="font-family:'Raleway',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
      <tr>
        <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:30px 10px 0px;font-family:'Raleway',sans-serif;" align="left">
          
    <!--[if mso]><table width="100%"><tr><td><![endif]-->
      <h1 class="v-text-align v-line-height v-font-size" style="margin: 0px; color: #b9ff66; line-height: 120%; text-align: left; word-wrap: break-word; font-family: Epilogue; font-size: 20px; font-weight: 400;"><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span>USER DETAILS</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h1>
    <!--[if mso]></td></tr></table><![endif]-->

        </td>
      </tr>
    </tbody>
  </table>

  <table style="font-family:'Raleway',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
      <tr>
        <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:10px 10px 10px 0px;font-family:'Raleway',sans-serif;" align="left">
          
    <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #777777;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
      <tbody>
        <tr style="vertical-align: top">
          <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
            <span>&#160;</span>
          </td>
        </tr>
      </tbody>
    </table>

        </td>
      </tr>
    </tbody>
  </table>

  <table style="font-family:'Raleway',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
      <tr>
        <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:10px 20px 0px 10px;font-family:'Raleway',sans-serif;" align="left">
          
    <div class="v-text-align v-line-height v-font-size" style="font-family: 'Raleway',sans-serif; font-size: 14px; color: #ffffff; line-height: 140%; text-align: left; word-wrap: break-word;">
      <p style="line-height: 140%;"><strong>Name: {name}</strong></p>
    </div>

        </td>
      </tr>
    </tbody>
  </table>

  <table id="u_content_text_1" style="font-family:'Raleway',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
      <tr>
        <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Raleway',sans-serif;" align="left">
          
    <div class="v-text-align v-line-height v-font-size" style="font-family: Epilogue; font-size: 14px; color: #ffffff; line-height: 140%; text-align: left; word-wrap: break-word;">
      <p style="line-height: 140%;"><strong>Case Id: {Id}</strong></p>
    </div>

        </td>
      </tr>
    </tbody>
  </table>

  <table id="u_content_text_12" style="font-family:'Raleway',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
      <tr>
        <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Raleway',sans-serif;" align="left">
          
    <div class="v-text-align v-line-height v-font-size" style="font-family: Epilogue; font-size: 14px; color: #ffffff; line-height: 140%; text-align: left; word-wrap: break-word;">
      <p style="line-height: 140%;"><strong>Mail id: {mail}</strong></p>
    </div>

        </td>
      </tr>
    </tbody>
  </table>

  <table id="u_content_text_13" style="font-family:'Raleway',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
      <tr>
        <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Raleway',sans-serif;" align="left">
          
    <div class="v-text-align v-line-height v-font-size" style="font-family: Epilogue; font-size: 14px; color: #ffffff; line-height: 140%; text-align: left; word-wrap: break-word;">
      <p style="line-height: 140%;"><strong>Gender: {gender}</strong></p>
    </div>

        </td>
      </tr>
    </tbody>
  </table>

  <table id="u_content_text_13" style="font-family:'Raleway',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
      <tr>
        <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Raleway',sans-serif;" align="left">
          
    <div class="v-text-align v-line-height v-font-size" style="font-family: Epilogue; font-size: 14px; color: #ffffff; line-height: 140%; text-align: left; word-wrap: break-word;">
      <p style="line-height: 140%;"><strong>Age: {age}</strong></p>
    </div>

        </td>
      </tr>
    </tbody>
  </table>

    <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
    </div>
  </div>
  <!--[if (mso)|(IE)]></td><![endif]-->
  <!--[if (mso)|(IE)]><td align="center" width="400" class="v-col-border" style="background-color: #1c1c1c;width: 400px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;" valign="top"><![endif]-->
  <div class="u-col u-col-66p67" style="max-width: 320px;min-width: 400px;display: table-cell;vertical-align: top;">
    <div style="background-color: #1c1c1c;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
    <!--[if (!mso)&(!IE)]><!--><div class="v-col-border" style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;"><!--<![endif]-->
    
  <table id="u_content_heading_2" style="font-family:'Raleway',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
      <tr>
        <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:125px 10px 0px;font-family:'Raleway',sans-serif;" align="left">
          
    <!--[if mso]><table width="100%"><tr><td><![endif]-->
      <h1 class="v-text-align v-line-height v-font-size" style="margin: 0px; color: #b9ff66; line-height: 120%; text-align: left; word-wrap: break-word; font-family: Epilogue; font-size: 55px; font-weight: 400;"><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span>DEEP TUMOR</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h1>
    <!--[if mso]></td></tr></table><![endif]-->

        </td>
      </tr>
    </tbody>
  </table>

  <table style="font-family:'Raleway',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
      <tr>
        <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:10px 30px 10px 10px;font-family:'Raleway',sans-serif;" align="left">
          
    <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #777777;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
      <tbody>
        <tr style="vertical-align: top">
          <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
            <span>&#160;</span>
          </td>
        </tr>
      </tbody>
    </table>

        </td>
      </tr>
    </tbody>
  </table>

  <table style="font-family:'Raleway',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
      <tr>
        <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:10px 20px 0px 10px;font-family:'Raleway',sans-serif;" align="left">
          
    <div class="v-text-align v-line-height v-font-size" style="font-family: 'Raleway',sans-serif; font-size: 14px; color: #95a5a6; line-height: 140%; text-align: left; word-wrap: break-word;">
      <p style="line-height: 140%;">The DeepTumor report email provides a comprehensive analysis of brain MRI images. It includes detailed findings on tumor segmentation and classification, with insights into tumor type, shape, and location.</p>
    </div>

        </td>
      </tr>
    </tbody>
  </table>


    <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
    </div>
  </div>
      </div>
    </div>
    </div>
    


    
    
    <div class="u-row-container" style="padding: 0px;background-color: transparent">
      <div class="u-row" style="margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
        <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
          <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: transparent;"><![endif]-->
          
    <!--[if (mso)|(IE)]><td align="center" width="600" class="v-col-border" style="background-color: #1c1c1c;width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;" valign="top"><![endif]-->
    <div class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
      <div style="background-color: #1c1c1c;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
      <!--[if (!mso)&(!IE)]><!--><div class="v-col-border" style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;"><!--<![endif]-->
      
    <table style="font-family:'Raleway',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
      <tbody>
        <tr>
          <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:20px;font-family:'Raleway',sans-serif;" align="left">
            
      <div class="v-text-align v-line-height v-font-size" style="font-size: 14px; line-height: 140%; text-align: center; word-wrap: break-word;">
        <p style="line-height: 140%;"></p>
      
    <div class="container">
      <h2>In Collaboration with</h2>
      <h1>Tars.Ai</h1>
  </div>
    
      </div>
    
          </td>
        </tr>
      </tbody>
    </table>
    
      <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
      </div>
    </div>

        </div>
      </div>
    </div>
    
    


    
    
  <div class="u-row-container" style="padding: 0px;background-color: transparent">
    <div class="u-row" style="margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
      <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
        
  <div class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
    <div style="background-color: #b9ff66;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
    <!--[if (!mso)&(!IE)]><!--><div class="v-col-border" style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 10px solid #1c1c1c;border-right: 10px solid #1c1c1c;border-bottom: 10px solid #1c1c1c;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;"><!--<![endif]-->
    
  <table id="u_content_heading_8" style="font-family:'Raleway',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
      <tr>
        <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:30px 10px 5px;font-family:'Raleway',sans-serif;" align="left">
          
      <h1 class="v-text-align v-line-height v-font-size" style="margin: 0px; line-height: 140%; text-align: center; word-wrap: break-word; font-family: Epilogue; font-size: 22px; font-weight: 400;"><span><span><span><span><span><span><span><span><strong>Brain Tumor Analysis</strong></span></span></span></span></span></span></span></span></h1>

        </td>
      </tr>
    </tbody>
  </table>

  <table id="u_content_text_2" style="font-family:'Raleway',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
      <tr>
        <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:0px 60px;font-family:'Raleway',sans-serif;" align="left">
          
    <div class="v-text-align v-line-height v-font-size" style="font-family: 'Raleway',sans-serif; font-size: 14px; line-height: 140%; text-align: left; word-wrap: break-word;">
      <p style="line-height: 140%; word-wrap: break-word; font-family: Epilogue; font-size: 15px; font-weight: 200;"><strong>Tumor status: {status}</strong></p>
  <p style="line-height: 140%; word-wrap: break-word; font-family: Epilogue; font-size: 15px; font-weight: 200;"><strong>Tumor length(in mm): {length}mm</strong></p>
  <p style="line-height: 140%; word-wrap: break-word; font-family: Epilogue; font-size: 15px; font-weight: 200;"><strong>Tumor breadth(in mm): {breadth}mm</strong></p>
  <p style="line-height: 140%; word-wrap: break-word; font-family: Epilogue; font-size: 15px; font-weight: 200;"><strong>Tumor Area(in mm square): {area}mm^2</strong></p>
  <p style="line-height: 140%; word-wrap: break-word; font-family: Epilogue; font-size: 15px; font-weight: 200;"><strong>Tumor location: {location}</strong></p>
  <p style="line-height: 140%; word-wrap: break-word; font-family: Epilogue; font-size: 15px; font-weight: 200;"><strong>Tumor stage: {stage}</strong></p>
  <p style="line-height: 140%; word-wrap: break-word; font-family: Epilogue; font-size: 15px; font-weight: 200;"><strong>Description: {description}<br></strong></p>
  <p style="line-height: 140%; word-wrap: break-word; font-family: Epilogue; font-size: 15px; font-weight: 200;"><strong>What to Do: {wtd}</strong></p>
  <p style="line-height: 140%; word-wrap: break-word; font-family: Epilogue; font-size: 15px; font-weight: 200;"><strong>Who to consult: {wtc}</strong></p>
  </div>

        </td>
      </tr>
    </tbody>
  </table>

  <table id="u_content_button_2" style="font-family:'Raleway',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
      <tr>
        <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:10px 10px 30px;font-family:'Raleway',sans-serif;" align="left">
          
  <div class="v-text-align" align="center">
  <v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="https://unlayer.com" style="height:37px; width:237px;" arcsize="11%" stroke="f" fillcolor="#1c1c1c"><w:anchorlock/><center style="color:#FFFFFF;">
      <a href="https://chat.openai.com" target="_blank" class="v-button v-size-width v-font-size" style="box-sizing: border-box;display: inline-block;text-decoration: none;-webkit-text-size-adjust: none;text-align: center;color: #FFFFFF; background-color: #1c1c1c; border-radius: 4px;-webkit-border-radius: 4px; -moz-border-radius: 4px; width:auto; max-width:100%; overflow-wrap: break-word; word-break: break-word; word-wrap:break-word;font-size: 11px;">
        <span class="v-line-height" style="display:block;padding:4px 10px;line-height:120%;"><span style="line-height: 16.8px;">Click and prompt for more info</span></span>
      </a>
  </div>

        </td>
      </tr>
    </tbody>
  </table>

    <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
    </div>
  </div>
      </div>
    </div>
    </div>
    


    
  <div class="u-row-container" style="padding: 0px;background-color: transparent">
    <div class="u-row" style="margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
      <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: transparent;"><![endif]-->
        
  <!--[if (mso)|(IE)]><td align="center" width="600" class="v-col-border" style="background-color: #1c1c1c;width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;" valign="top"><![endif]-->
  <div class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
    <div style="background-color: #1c1c1c;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
    <!--[if (!mso)&(!IE)]><!--><div class="v-col-border" style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;"><!--<![endif]-->
    
  <table id="u_content_heading_9" style="font-family:'Raleway',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
      <tr>
        <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:40px 10px 10px 40px;font-family:'Raleway',sans-serif;" align="left">
          
    <!--[if mso]><table width="100%"><tr><td><![endif]-->
      <h1 class="v-text-align v-line-height v-font-size" style="margin: 0px; color: #b9ff66; line-height: 120%; text-align: left; word-wrap: break-word; font-family: Epilogue; font-size: 20px; font-weight: 400;"><span><strong>Thanks for choosing us!! 🗿</strong></span></h1>
    <!--[if mso]></td></tr></table><![endif]-->

        </td>
      </tr>
    </tbody>
  </table>

  <table id="u_content_text_10" style="font-family:'Raleway',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
      <tr>
        <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:10px 60px 25px 40px;font-family:'Raleway',sans-serif;" align="left">
          
    <div class="v-text-align v-line-height v-font-size" style="font-size: 14px; color: #b8b8b8; line-height: 170%; text-align: left; word-wrap: break-word;">
      <p style="line-height: 170%;"><span data-metadata="&lt;!--(figmeta)eyJmaWxlS2V5IjoiaUdkbDhwdlZkTlBQU2x2aTlkeXpHRyIsInBhc3RlSUQiOjMxOTY0Mjc2NCwiZGF0YVR5cGUiOiJzY2VuZSJ9Cg==(/figmeta)--&gt;" style="line-height: 23.8px;">We wanted to take a moment to express our sincere gratitude for choosing deeptumor for your health journey. </span></p>
  <p style="line-height: 170%;"><span style="line-height: 23.8px;"><br />Please reach out to us if you have any thoughts, praise, or custom project to <a rel="noopener" href="mailto:bharath.sudarsanam04@gmail.com?subject=Support%20%26%20Query" target="_blank">bharath.sudarsanam04@gmail.com</a>. We’d love to hear from you!</span></p>
    </div>

        </td>
      </tr>
    </tbody>
  </table>

  <table id="u_content_social_1" style="font-family:'Raleway',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
      <tr>
        <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:0px 10px 20px 40px;font-family:'Raleway',sans-serif;" align="left">
          
  <div align="left">
    <div style="display: table; max-width:125px;">    
      <table align="left" border="0" cellspacing="0" cellpadding="0" width="32" height="32" style="width: 32px !important;height: 32px !important;display: inline-block;border-collapse: collapse;table-layout: fixed;border-spacing: 0;vertical-align: top;margin-right: 10px">
        <tbody><tr style="vertical-align: top"><td align="left" valign="middle" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
          <a href="https://www.linkedin.com/in/bharath-sudarsanam/" title="LinkedIn" target="_blank">
              <a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/G9W7W0ML/image-1.png" alt="LinkedIn" title="LinkedIn" width="32" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: none;height: auto;float: none;max-width: 32px !important"/></a><br/><br/>
          </a>
        </td></tr>
      </tbody></table>
      
      <table align="left" border="0" cellspacing="0" cellpadding="0" width="32" height="32" style="width: 32px !important;height: 32px !important;display: inline-block;border-collapse: collapse;table-layout: fixed;border-spacing: 0;vertical-align: top;margin-right: 10px">
        <tbody><tr style="vertical-align: top"><td align="left" valign="middle" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
          <a href="https://www.instagram.com/__itz.me.bharath__/" title="Instagram" target="_blank">
              <a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/rDJfRDqs/image-3.png" alt="Instagram" title="Instagram" width="32" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: none;height: auto;float: none;max-width: 32px !important"/></a><br/><br/>
          </a>
        </td></tr>
      </tbody></table>    
      <table align="left" border="0" cellspacing="0" cellpadding="0" width="32" height="32" style="width: 32px !important;height: 32px !important;display: inline-block;border-collapse: collapse;table-layout: fixed;border-spacing: 0;vertical-align: top;margin-right: 0px">
        <tbody><tr style="vertical-align: top"><td align="left" valign="middle" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
          <a href="https://github.com/Bharath-tars" title="GitHub" target="_blank">
              <a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/ph9CSkz5/image-4.png" alt="GitHub" title="GitHub" width="32" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: none;height: auto;float: none;max-width: 32px !important"/></a><br/><br/>
          </a>
        </td></tr>
      </tbody></table>
    </div>
  </div>

        </td>
      </tr>
    </tbody>
  </table>

  <table style="font-family:'Raleway',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
      <tr>
        <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:10px 10px 0px;font-family:'Raleway',sans-serif;" align="left">
          
    <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="92%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
      <tbody>
        <tr style="vertical-align: top">
          <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
            <span>&#160;</span>
          </td>
        </tr>
      </tbody>
    </table>

        </td>
      </tr>
    </tbody>
  </table>

    <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
    </div>
  </div>
      </div>
    </div>
    </div>
    
  <div class="u-row-container" style="padding: 0px;background-color: transparent">
    <div class="u-row" style="margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
      <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
        
  <div class="u-col u-col-62p26" style="max-width: 320px;min-width: 373.56px;display: table-cell;vertical-align: top;">
    <div style="background-color: #1c1c1c;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
    <!--[if (!mso)&(!IE)]><!--><div class="v-col-border" style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;"><!--<![endif]-->
    
  <table id="u_content_text_11" style="font-family:'Raleway',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
      <tr>
        <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:20px 10px 20px 40px;font-family:'Raleway',sans-serif;" align="left">
          
    <div class="v-text-align v-line-height v-font-size" style="font-size: 13px; color: #ffffff; line-height: 140%; text-align: left; word-wrap: break-word;">
      <p style="line-height: 140%;">Made with ❣ by Sudarsanam Bharath</p>
    </div>

        </td>
      </tr>
    </tbody>
  </table>

    <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
    </div>
  </div>
  <div class="u-col u-col-37p74" style="max-width: 320px;min-width: 226.44px;display: table-cell;vertical-align: top;">
    <div style="background-color: #1c1c1c;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
    <!--[if (!mso)&(!IE)]><!--><div class="v-col-border" style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;"><!--<![endif]-->
    
  <table id="u_content_image_4" style="font-family:'Raleway',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
      <tr>
        <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:10px 30px 10px 10px;font-family:'Raleway',sans-serif;" align="left">
  <table width="100%" cellpadding="0" cellspacing="0" border="0">
    <tr>
      <td class="v-text-align" style="padding-right: 0px;padding-left: 0px;" align="right">
      </td>
    </tr>
  </table>
        </td>
      </tr>
    </tbody>
  </table>
    <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
    </div>
  </div>
      </div>
    </div>
    </div>
      <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
      </td>
    </tr>
    </tbody>
    </table>
  </body>

  </html>
  """
  subject = f"{number} | DeepTumor Cancer Detection & Analysis Report"
  variables = {
      "name": real_name,
      "Id": number,
      "mail": mail,
      "age": age,
      "gender": gender,
      "stage": result,
      "length": length,
      "breadth": width,
      "area": area,
      "location": location,
      "status": status,
      "description": decription,
      "wtd": wtd,
      "wtc": wtc
  }
  html_content = html_template.format(**variables)
  # Example usage
  from_email = "bharathworks2u@gmail.com"
  password = "yiyiqhgtovmjoxeq"

      # Set up the MIME
  msg = MIMEMultipart('alternative')
  msg['From'] = from_email
  msg['To'] = mail
  msg['Subject'] = subject

      # Attach the HTML content
  msg.attach(MIMEText(html_content, 'html'))

      # Create a secure SSL context
  context = smtplib.ssl.create_default_context()

      # Sending the email
  try:
      with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
              server.login(from_email, password)
              server.sendmail(from_email, mail, msg.as_string())
              print("Email sent successfully!")
  except Exception as e:
          print(f"Failed to send email: {e}")

  return "Email sent successfully!"