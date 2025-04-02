import json
from urllib import request
import time

# URL da API do ComfyUI
COMFYUI_API_URL = "http://127.0.0.1:8188"


def setWorkflowMochi(len, wid, hei, fps, crf, cfg, prompt):
    
    name = str(len)+"_"+str(wid)+"_"+str(hei)+"_"+str(fps)+"_"+str(crf)+"_"+str(cfg)+"_"+"Mochi"

    # Definição do workflow (substitua conforme necessário)
    workflow = {
    "1": {
        "inputs": {
        "clip_name": "t5xxl_fp16.safetensors",
        "type": "mochi",
        "device": "default"
        },
        "class_type": "CLIPLoader",
        "_meta": {
        "title": "Load CLIP"
        }
    },
    "2": {
        "inputs": {
        "unet_name": "mochi_preview_bf16.safetensors",
        "weight_dtype": "default"
        },
        "class_type": "UNETLoader",
        "_meta": {
        "title": "Load Diffusion Model"
        }
    },
    "3": {
        "inputs": {
        "text":  prompt,
        "clip": [
            "1",
            0
        ]
        },
        "class_type": "CLIPTextEncode",
        "_meta": {
        "title": "CLIP Text Encode (Prompt)"
        }
    },
    "4": {
        "inputs": {
        "text": "",
        "clip": [
            "1",
            0
        ]
        },
        "class_type": "CLIPTextEncode",
        "_meta": {
        "title": "CLIP Text Encode (Prompt)"
        }
    },
    "5": {
        "inputs": {
        "seed": 898052028774897,
        "steps": 30,
        "cfg": cfg,
        "sampler_name": "euler",
        "scheduler": "simple",
        "denoise": 1,
        "model": [
            "2",
            0
        ],
        "positive": [
            "3",
            0
        ],
        "negative": [
            "4",
            0
        ],
        "latent_image": [
            "7",
            0
        ]
        },
        "class_type": "KSampler",
        "_meta": {
        "title": "KSampler"
        }
    },
    "6": {
        "inputs": {
        "vae_name": "mochi_vae.safetensors"
        },
        "class_type": "VAELoader",
        "_meta": {
        "title": "Load VAE"
        }
    },
    "7": {
        "inputs": {
        "width": wid,
        "height": hei,
        "length": len,
        "batch_size": 1
        },
        "class_type": "EmptyCosmosLatentVideo",
        "_meta": {
        "title": "EmptyCosmosLatentVideo"
        }
    },
    "8": {
        "inputs": {
        "samples": [
            "5",
            0
        ],
        "vae": [
            "6",
            0
        ]
        },
        "class_type": "VAEDecode",
        "_meta": {
        "title": "VAE Decode"
        }
    },
    "9": {
        "inputs": {
        "filename_prefix": name,
        "codec": "vp9",
        "fps": fps,
        "crf": crf,
        "images": [
            "8",
            0
        ]
        },
        "class_type": "SaveWEBM",
        "_meta": {
        "title": "SaveWEBM"
        }
    }
  
    }

    return workflow



def setWorkflowLX(len, wid, hei, fps, crf, cfg, prompt):
    
    name = str(len)+"_"+str(wid)+"_"+str(hei)+"_"+str(fps)+"_"+str(crf)+"_"+str(cfg)+"_"+"LX_Text"
    
    workflow = {
  "6": {
    "inputs": {
      "text":  prompt,      "clip": [
        "38",
        0
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Positive Prompt)"
    }
  },
  "7": {
    "inputs": {
      "text": "色调艳丽，过曝，静态，细节模糊不清，字幕，风格，作品，画作，画面，静止，整体发灰，最差质量，低质量，JPEG压缩残留，丑陋的，残缺的，多余的手指，画得不好的手部，画得不好的脸部，畸形的，毁容的，形态畸形的肢体，手指融合，静止不动的画面，杂乱的背景，三条腿，背景人很多，倒着走",
      "clip": [
        "38",
        0
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Negative Prompt)"
    }
  },
  "8": {
    "inputs": {
      "samples": [
        "72",
        0
      ],
      "vae": [
        "44",
        2
      ]
    },
    "class_type": "VAEDecode",
    "_meta": {
      "title": "VAE Decode"
    }
  },
  "38": {
    "inputs": {
      "clip_name": "t5xxl_fp16.safetensors",
      "type": "ltxv",
      "device": "default"
    },
    "class_type": "CLIPLoader",
    "_meta": {
      "title": "Load CLIP"
    }
  },
  "44": {
    "inputs": {
      "ckpt_name": "ltx-video-2b-v0.9.5.safetensors"
    },
    "class_type": "CheckpointLoaderSimple",
    "_meta": {
      "title": "Load Checkpoint"
    }
  },
  "69": {
    "inputs": {
      "frame_rate": 25,
      "positive": [
        "6",
        0
      ],
      "negative": [
        "7",
        0
      ]
    },
    "class_type": "LTXVConditioning",
    "_meta": {
      "title": "LTXVConditioning"
    }
  },
  "70": {
    "inputs": {
      "width": wid,
      "height": hei,
      "length": len,
      "batch_size": 1
    },
    "class_type": "EmptyLTXVLatentVideo",
    "_meta": {
      "title": "EmptyLTXVLatentVideo"
    }
  },
  "71": {
    "inputs": {
      "steps": 30,
      "max_shift": 2.05,
      "base_shift": 0.95,
      "stretch": True,
      "terminal": 0.1,
      "latent": [
        "70",
        0
      ]
    },
    "class_type": "LTXVScheduler",
    "_meta": {
      "title": "LTXVScheduler"
    }
  },
  "72": {
    "inputs": {
      "add_noise": True,
      "noise_seed": 261471249254103,
      "cfg":cfg,
      "model": [
        "44",
        0
      ],
      "positive": [
        "69",
        0
      ],
      "negative": [
        "69",
        1
      ],
      "sampler": [
        "73",
        0
      ],
      "sigmas": [
        "71",
        0
      ],
      "latent_image": [
        "70",
        0
      ]
    },
    "class_type": "SamplerCustom",
    "_meta": {
      "title": "SamplerCustom"
    }
  },
  "73": {
    "inputs": {
      "sampler_name": "euler"
    },
    "class_type": "KSamplerSelect",
    "_meta": {
      "title": "KSamplerSelect"
    }
  },
  "78": {
    "inputs": {
      "filename_prefix": name,
      "codec": "vp9",
      "fps": fps,
      "crf": crf,
      "images": [
        "8",
        0
      ]
    },
    "class_type": "SaveWEBM",
    "_meta": {
      "title": "SaveWEBM"
    }
  }
}

    return workflow

def setWorkflowWan3(len, wid, hei, fps, crf, cfg, prompt):
    
    name = str(len)+"_"+str(wid)+"_"+str(hei)+"_"+str(fps)+"_"+str(crf)+"_"+str(cfg)+"_"+"Wan3"
    
    workflow = {
  "3": {
    "inputs": {
      "seed": 682045780498416,
      "steps": 30,
      "cfg": cfg,
      "sampler_name": "uni_pc",
      "scheduler": "simple",
      "denoise": 1,
      "model": [
        "48",
        0
      ],
      "positive": [
        "6",
        0
      ],
      "negative": [
        "7",
        0
      ],
      "latent_image": [
        "40",
        0
      ]
    },
    "class_type": "KSampler",
    "_meta": {
      "title": "KSampler"
    }
  },
  "6": {
    "inputs": {
      "text":  prompt,      "clip": [
        "38",
        0
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Positive Prompt)"
    }
  },
  "7": {
    "inputs": {
      "text": "",
      "clip": [
        "38",
        0
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Negative Prompt)"
    }
  },
  "8": {
    "inputs": {
      "samples": [
        "3",
        0
      ],
      "vae": [
        "39",
        0
      ]
    },
    "class_type": "VAEDecode",
    "_meta": {
      "title": "VAE Decode"
    }
  },
  "37": {
    "inputs": {
      "unet_name": "wan2.1_t2v_1.3B_fp16.safetensors",
      "weight_dtype": "default"
    },
    "class_type": "UNETLoader",
    "_meta": {
      "title": "Load Diffusion Model"
    }
  },
  "38": {
    "inputs": {
      "clip_name": "umt5_xxl_fp8_e4m3fn_scaled.safetensors",
      "type": "wan",
      "device": "default"
    },
    "class_type": "CLIPLoader",
    "_meta": {
      "title": "Load CLIP"
    }
  },
  "39": {
    "inputs": {
      "vae_name": "wan_2.1_vae.safetensors"
    },
    "class_type": "VAELoader",
    "_meta": {
      "title": "Load VAE"
    }
  },
  "40": {
    "inputs": {
      "width": wid,
      "height": hei,
      "length": len,
      "batch_size": 1
    },
    "class_type": "EmptyHunyuanLatentVideo",
    "_meta": {
      "title": "EmptyHunyuanLatentVideo"
    }
  },
  "48": {
    "inputs": {
      "shift": 8,
      "model": [
        "37",
        0
      ]
    },
    "class_type": "ModelSamplingSD3",
    "_meta": {
      "title": "ModelSamplingSD3"
    }
  },
  "49": {
    "inputs": {
      "filename_prefix": name,
      "codec": "vp9",
      "fps": fps,
      "crf": crf,
      "images": [
        "8",
        0
      ]
    },
    "class_type": "SaveWEBM",
    "_meta": {
      "title": "SaveWEBM"
    }
  }
}

    return workflow


def setWorkflowWan14(len, wid, hei, fps, crf, cfg, prompt):
    
    name = str(len)+"_"+str(wid)+"_"+str(hei)+"_"+str(fps)+"_"+str(crf)+"_"+str(cfg)+"_"+"Wan14"
    
    workflow = {
  "3": {
    "inputs": {
      "seed": 682045780498416,
      "steps": 30,
      "cfg": cfg,
      "sampler_name": "uni_pc",
      "scheduler": "simple",
      "denoise": 1,
      "model": [
        "48",
        0
      ],
      "positive": [
        "6",
        0
      ],
      "negative": [
        "7",
        0
      ],
      "latent_image": [
        "40",
        0
      ]
    },
    "class_type": "KSampler",
    "_meta": {
      "title": "KSampler"
    }
  },
  "6": {
    "inputs": {
      "text": prompt,
      "clip": [
        "38",
        0
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Positive Prompt)"
    }
  },
  "7": {
    "inputs": {
      "text": "",
      "clip": [
        "38",
        0
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Negative Prompt)"
    }
  },
  "8": {
    "inputs": {
      "samples": [
        "3",
        0
      ],
      "vae": [
        "39",
        0
      ]
    },
    "class_type": "VAEDecode",
    "_meta": {
      "title": "VAE Decode"
    }
  },
  "37": {
    "inputs": {
      "unet_name": "wan2.1_t2v_14B_fp16.safetensors",
      "weight_dtype": "default"
    },
    "class_type": "UNETLoader",
    "_meta": {
      "title": "Load Diffusion Model"
    }
  },
  "38": {
    "inputs": {
      "clip_name": "umt5_xxl_fp8_e4m3fn_scaled.safetensors",
      "type": "wan",
      "device": "default"
    },
    "class_type": "CLIPLoader",
    "_meta": {
      "title": "Load CLIP"
    }
  },
  "39": {
    "inputs": {
      "vae_name": "wan_2.1_vae.safetensors"
    },
    "class_type": "VAELoader",
    "_meta": {
      "title": "Load VAE"
    }
  },
  "40": {
    "inputs": {
      "width": wid,
      "height": hei,
      "length": len,
      "batch_size": 1
    },
    "class_type": "EmptyHunyuanLatentVideo",
    "_meta": {
      "title": "EmptyHunyuanLatentVideo"
    }
  },
  "48": {
    "inputs": {
      "shift": 8,
      "model": [
        "37",
        0
      ]
    },
    "class_type": "ModelSamplingSD3",
    "_meta": {
      "title": "ModelSamplingSD3"
    }
  },
  "49": {
    "inputs": {
      "filename_prefix": name,
      "codec": "vp9",
      "fps": fps,
      "crf": crf,
      "images": [
        "8",
        0
      ]
    },
    "class_type": "SaveWEBM",
    "_meta": {
      "title": "SaveWEBM"
    }
  }
}

    return workflow

def setWorkflowLTXIMAGEM(len, wid, hei, fps, crf, cfg, prompt):
    
    name = str(len)+"_"+str(wid)+"_"+str(hei)+"_"+str(fps)+"_"+str(crf)+"_"+str(cfg)+"_"+"LTX_Image"
    
    workflow = {
  "6": {
    "inputs": {
      "text": prompt,
      "clip": [
        "38",
        0
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Positive Prompt)"
    }
  },
  "7": {
    "inputs": {
      "text": "low quality, worst quality, deformed, distorted, disfigured, motion smear, motion artifacts, fused fingers, bad anatomy, weird hand, ugly, not fusion",
      "clip": [
        "38",
        0
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Negative Prompt)"
    }
  },
  "8": {
    "inputs": {
      "samples": [
        "72",
        0
      ],
      "vae": [
        "44",
        2
      ]
    },
    "class_type": "VAEDecode",
    "_meta": {
      "title": "VAE Decode"
    }
  },
  "38": {
    "inputs": {
      "clip_name": "t5xxl_fp16.safetensors",
      "type": "ltxv",
      "device": "default"
    },
    "class_type": "CLIPLoader",
    "_meta": {
      "title": "Load CLIP"
    }
  },
  "44": {
    "inputs": {
      "ckpt_name": "ltx-video-2b-v0.9.5.safetensors"
    },
    "class_type": "CheckpointLoaderSimple",
    "_meta": {
      "title": "Load Checkpoint"
    }
  },
  "69": {
    "inputs": {
      "frame_rate": 25,
      "positive": [
        "95",
        0
      ],
      "negative": [
        "95",
        1
      ]
    },
    "class_type": "LTXVConditioning",
    "_meta": {
      "title": "LTXVConditioning"
    }
  },
  "71": {
    "inputs": {
      "steps": 30,
      "max_shift": 2.05,
      "base_shift": 0.95,
      "stretch": True,
      "terminal": 0.1,
      "latent": [
        "95",
        2
      ]
    },
    "class_type": "LTXVScheduler",
    "_meta": {
      "title": "LTXVScheduler"
    }
  },
  "72": {
    "inputs": {
      "add_noise": True,
      "noise_seed": 28364341343355,
      "cfg": cfg,
      "model": [
        "44",
        0
      ],
      "positive": [
        "69",
        0
      ],
      "negative": [
        "69",
        1
      ],
      "sampler": [
        "73",
        0
      ],
      "sigmas": [
        "71",
        0
      ],
      "latent_image": [
        "95",
        2
      ]
    },
    "class_type": "SamplerCustom",
    "_meta": {
      "title": "SamplerCustom"
    }
  },
  "73": {
    "inputs": {
      "sampler_name": "euler"
    },
    "class_type": "KSamplerSelect",
    "_meta": {
      "title": "KSamplerSelect"
    }
  },
  "78": {
    "inputs": {
      "image": "teste3.png"
    },
    "class_type": "LoadImage",
    "_meta": {
      "title": "Load Image"
    }
  },
  "82": {
    "inputs": {
      "img_compression": 40,
      "image": [
        "78",
        0
      ]
    },
    "class_type": "LTXVPreprocess",
    "_meta": {
      "title": "LTXVPreprocess"
    }
  },
  "95": {
    "inputs": {
      "width": wid,
      "height": hei,
      "length": len,
      "batch_size": 1,
      "positive": [
        "6",
        0
      ],
      "negative": [
        "7",
        0
      ],
      "vae": [
        "44",
        2
      ],
      "image": [
        "82",
        0
      ]
    },
    "class_type": "LTXVImgToVideo",
    "_meta": {
      "title": "LTXVImgToVideo"
    }
  },
  "96": {
    "inputs": {
      "filename_prefix": name,
      "codec": "vp9",
      "fps": fps,
      "crf": crf,
      "images": [
        "8",
        0
      ]
    },
    "class_type": "SaveWEBM",
    "_meta": {
      "title": "SaveWEBM"
    }
  }
}

    return workflow

def setWorkflowFinish(prompt, num_scene, id):
     
    workflow = {
  "6": {
    "inputs": {
      "text":  prompt + "The scene is animated in a whimsical Disney style, with bright, cheerful colors that evoke a sense of joy and magic in this fantastical setting.",
        "clip": [
        "38",
        0
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Positive Prompt)"
    }
  },
  "7": {
    "inputs": {
      "text": "色调艳丽，过曝，静态，细节模糊不清，字幕，风格，作品，画作，画面，静止，整体发灰，最差质量，低质量，JPEG压缩残留，丑陋的，残缺的，多余的手指，画得不好的手部，画得不好的脸部，畸形的，毁容的，形态畸形的肢体，手指融合，静止不动的画面，杂乱的背景，三条腿，背景人很多，倒着走",
      "clip": [
        "38",
        0
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Negative Prompt)"
    }
  },
  "8": {
    "inputs": {
      "samples": [
        "72",
        0
      ],
      "vae": [
        "44",
        2
      ]
    },
    "class_type": "VAEDecode",
    "_meta": {
      "title": "VAE Decode"
    }
  },
  "38": {
    "inputs": {
      "clip_name": "t5xxl_fp16.safetensors",
      "type": "ltxv",
      "device": "default"
    },
    "class_type": "CLIPLoader",
    "_meta": {
      "title": "Load CLIP"
    }
  },
  "44": {
    "inputs": {
      "ckpt_name": "ltx-video-2b-v0.9.5.safetensors"
    },
    "class_type": "CheckpointLoaderSimple",
    "_meta": {
      "title": "Load Checkpoint"
    }
  },
  "69": {
    "inputs": {
      "frame_rate": 25,
      "positive": [
        "6",
        0
      ],
      "negative": [
        "7",
        0
      ]
    },
    "class_type": "LTXVConditioning",
    "_meta": {
      "title": "LTXVConditioning"
    }
  },
  "70": {
    "inputs": {
      "width": 100,
      "height": 100,
      "length": 121,
      "batch_size": 1
    },
    "class_type": "EmptyLTXVLatentVideo",
    "_meta": {
      "title": "EmptyLTXVLatentVideo"
    }
  },
  "71": {
    "inputs": {
      "steps": 30,
      "max_shift": 2.05,
      "base_shift": 0.95,
      "stretch": True,
      "terminal": 0.1,
      "latent": [
        "70",
        0
      ]
    },
    "class_type": "LTXVScheduler",
    "_meta": {
      "title": "LTXVScheduler"
    }
  },
  "72": {
    "inputs": {
      "add_noise": True,
      "noise_seed": 261471249254103,
      "cfg":32,
      "model": [
        "44",
        0
      ],
      "positive": [
        "69",
        0
      ],
      "negative": [
        "69",
        1
      ],
      "sampler": [
        "73",
        0
      ],
      "sigmas": [
        "71",
        0
      ],
      "latent_image": [
        "70",
        0
      ]
    },
    "class_type": "SamplerCustom",
    "_meta": {
      "title": "SamplerCustom"
    }
  },
  "73": {
    "inputs": {
      "sampler_name": "euler"
    },
    "class_type": "KSamplerSelect",
    "_meta": {
      "title": "KSamplerSelect"
    }
  },
  "78": {
    "inputs": {
      "filename_prefix": id +"_"+num_scene+"_",
      "codec": "vp9",
      "fps": 24,
      "crf": 32,
      "images": [
        "8",
        0
      ]
    },
    "class_type": "SaveWEBM",
    "_meta": {
      "title": "SaveWEBM"
    }
  }
}

    return workflow


def sendWorkflow(prompt):
    print("Iniciando geração de video ...")
    # Enviar o workflow para a API do ComfyUI
    p = {"prompt": prompt}
    data = json.dumps(p).encode('utf-8')
    req = request.Request(f"{COMFYUI_API_URL}/prompt", data=data)
    response = request.urlopen(req)

def teste():
    
    ltximg = 3
    wan14 = 6
    wan3 = 6
    ltxText = 3
    mochi = 4.5
    

    prompt = "A little girl with curly brown hair, wearing a bright pink dress adorned with sparkles, stands in a vibrant toy store filled with shiny toys and colorful sweets. She gazes wide-eyed at a dazzling array of stuffed animals, action figures, and candy jars that twinkle under the warm, golden lighting. The camera angle is a medium shot, capturing her excitement as she clutches a shiny coin in her small hands, her fingers curling around it tightly. Suddenly, her attention is drawn to a magical piggy bank in the shape of a star, located on a shelf to her right. The piggy bank glows softly with a rainbow of colors, its surface shimmering like a jewel. The camera zooms in for a close-up on the piggy bank as sparkles dance around it, creating an enchanting atmosphere. The background remains blurred, allowing the focus to remain on the girl’s expression of wonder and curiosity. The scene is animated in a whimsical Disney style, with bright, cheerful colors that evoke a sense of joy and magic in this fantastical setting."


    # width = 320
    # height = 240
    # len = 50
    # fps = 5
    # crf = 32
    # cfg_exc = 0




    # sendWorkflow(setWorkflowLTXIMAGEM(len,width,height,fps,crf,cfg_exc + ltximg, prompt))
    # sendWorkflow(setWorkflowLX(len,width,height,fps,crf,cfg_exc + ltxText, prompt))
    # sendWorkflow(setWorkflowMochi(len,width,height,fps,crf,cfg_exc + mochi, prompt))
    # sendWorkflow(setWorkflowWan3(len,width,height,fps,crf,cfg_exc + wan3, prompt))
    # sendWorkflow(setWorkflowWan14(len,width,height,fps,crf, cfg_exc + wan14,prompt))

    # width = 320
    # height = 240
    # len = 50
    # fps = 5
    # crf = 32
    # cfg_exc = 0.5


    # sendWorkflow(setWorkflowLTXIMAGEM(len,width,height,fps,crf,cfg_exc + ltximg, prompt))
    # sendWorkflow(setWorkflowLX(len,width,height,fps,crf,cfg_exc + ltxText, prompt))
    # sendWorkflow(setWorkflowMochi(len,width,height,fps,crf,cfg_exc + mochi, prompt))
    # sendWorkflow(setWorkflowWan3(len,width,height,fps,crf,cfg_exc + wan3, prompt))
    # sendWorkflow(setWorkflowWan14(len,width,height,fps,crf, cfg_exc + wan14,prompt))


    # width = 320
    # height = 240
    # len = 50
    # fps = 5
    # crf = 32
    # cfg_exc = 1


    # sendWorkflow(setWorkflowLTXIMAGEM(len,width,height,fps,crf,cfg_exc + ltximg, prompt))
    # sendWorkflow(setWorkflowLX(len,width,height,fps,crf,cfg_exc + ltxText, prompt))
    # sendWorkflow(setWorkflowMochi(len,width,height,fps,crf,cfg_exc + mochi, prompt))
    # sendWorkflow(setWorkflowWan3(len,width,height,fps,crf,cfg_exc + wan3, prompt))
    # sendWorkflow(setWorkflowWan14(len,width,height,fps,crf, cfg_exc + wan14,prompt))


    # width = 320
    # height = 240
    # len = 50
    # fps = 5
    # crf = 32
    # cfg_exc = -0.5



    # sendWorkflow(setWorkflowLTXIMAGEM(len,width,height,fps,crf,cfg_exc + ltximg, prompt))
    # sendWorkflow(setWorkflowLX(len,width,height,fps,crf,cfg_exc + ltxText, prompt))
    # sendWorkflow(setWorkflowMochi(len,width,height,fps,crf,cfg_exc + mochi, prompt))
    # sendWorkflow(setWorkflowWan3(len,width,height,fps,crf,cfg_exc + wan3, prompt))
    # sendWorkflow(setWorkflowWan14(len,width,height,fps,crf, cfg_exc + wan14,prompt))


    # width = 320
    # height = 240
    # len = 50
    # fps = 5
    # crf = 32
    # cfg_exc = -1



    # sendWorkflow(setWorkflowLTXIMAGEM(len,width,height,fps,crf,cfg_exc + ltximg, prompt))
    # sendWorkflow(setWorkflowLX(len,width,height,fps,crf,cfg_exc + ltxText, prompt))
    # sendWorkflow(setWorkflowMochi(len,width,height,fps,crf,cfg_exc + mochi, prompt))
    # sendWorkflow(setWorkflowWan3(len,width,height,fps,crf,cfg_exc + wan3, prompt))
    # sendWorkflow(setWorkflowWan14(len,width,height,fps,crf, cfg_exc + wan14,prompt))

    # ##########################

    # width = 320
    # height = 240
    # len = 96
    # fps = 5
    # crf = 32
    # cfg_exc = 0.5


    # sendWorkflow(setWorkflowLTXIMAGEM(len,width,height,fps,crf,cfg_exc + ltximg, prompt))
    # sendWorkflow(setWorkflowLX(len,width,height,fps,crf,cfg_exc + ltxText, prompt))
    # sendWorkflow(setWorkflowMochi(len,width,height,fps,crf,cfg_exc + mochi, prompt))
    # sendWorkflow(setWorkflowWan3(len,width,height,fps,crf,cfg_exc + wan3, prompt))
    # sendWorkflow(setWorkflowWan14(len,width,height,fps,crf, cfg_exc + wan14,prompt))


    # width = 320
    # height = 240
    # len = 96
    # fps = 5
    # crf = 32
    # cfg_exc = 1


    # sendWorkflow(setWorkflowLTXIMAGEM(len,width,height,fps,crf,cfg_exc + ltximg, prompt))
    # sendWorkflow(setWorkflowLX(len,width,height,fps,crf,cfg_exc + ltxText, prompt))
    # sendWorkflow(setWorkflowMochi(len,width,height,fps,crf,cfg_exc + mochi, prompt))
    # sendWorkflow(setWorkflowWan3(len,width,height,fps,crf,cfg_exc + wan3, prompt))
    # sendWorkflow(setWorkflowWan14(len,width,height,fps,crf, cfg_exc + wan14,prompt))


    # width = 320
    # height = 240
    # len = 96
    # fps = 5
    # crf = 32
    # cfg_exc = -0.5



    # sendWorkflow(setWorkflowLTXIMAGEM(len,width,height,fps,crf,cfg_exc + ltximg, prompt))
    # sendWorkflow(setWorkflowLX(len,width,height,fps,crf,cfg_exc + ltxText, prompt))
    # sendWorkflow(setWorkflowMochi(len,width,height,fps,crf,cfg_exc + mochi, prompt))
    # sendWorkflow(setWorkflowWan3(len,width,height,fps,crf,cfg_exc + wan3, prompt))
    # sendWorkflow(setWorkflowWan14(len,width,height,fps,crf, cfg_exc + wan14,prompt))


    # width = 320
    # height = 240
    # len = 96
    # fps = 5
    # crf = 32
    # cfg_exc = -1



    # sendWorkflow(setWorkflowLTXIMAGEM(len,width,height,fps,crf,cfg_exc + ltximg, prompt))
    # sendWorkflow(setWorkflowLX(len,width,height,fps,crf,cfg_exc + ltxText, prompt))
    # sendWorkflow(setWorkflowMochi(len,width,height,fps,crf,cfg_exc + mochi, prompt))
    # sendWorkflow(setWorkflowWan3(len,width,height,fps,crf,cfg_exc + wan3, prompt))
    # sendWorkflow(setWorkflowWan14(len,width,height,fps,crf, cfg_exc + wan14,prompt))

    # width = 640
    # height = 480
    # len = 50
    # fps = 5
    # crf = 32
    # cfg_exc = 0.5


    # sendWorkflow(setWorkflowLTXIMAGEM(len,width,height,fps,crf,cfg_exc + ltximg, prompt))
    # sendWorkflow(setWorkflowLX(len,width,height,fps,crf,cfg_exc + ltxText, prompt))
    # sendWorkflow(setWorkflowMochi(len,width,height,fps,crf,cfg_exc + mochi, prompt))
    # sendWorkflow(setWorkflowWan3(len,width,height,fps,crf,cfg_exc + wan3, prompt))
    # sendWorkflow(setWorkflowWan14(len,width,height,fps,crf, cfg_exc + wan14,prompt))






################################ Parou aqui             """"""""""""""""""""""""""










    width = 640
    height = 480
    len = 50
    fps = 5
    crf = 32
    cfg_exc = 1


    sendWorkflow(setWorkflowLTXIMAGEM(len,width,height,fps,crf,cfg_exc + ltximg, prompt))
    sendWorkflow(setWorkflowLX(len,width,height,fps,crf,cfg_exc + ltxText, prompt))
    sendWorkflow(setWorkflowMochi(len,width,height,fps,crf,cfg_exc + mochi, prompt))
    sendWorkflow(setWorkflowWan3(len,width,height,fps,crf,cfg_exc + wan3, prompt))
    sendWorkflow(setWorkflowWan14(len,width,height,fps,crf, cfg_exc + wan14,prompt))


    width = 640
    height = 480
    len = 50
    fps = 5
    crf = 32
    cfg_exc = -0.5



    sendWorkflow(setWorkflowLTXIMAGEM(len,width,height,fps,crf,cfg_exc + ltximg, prompt))
    sendWorkflow(setWorkflowLX(len,width,height,fps,crf,cfg_exc + ltxText, prompt))
    sendWorkflow(setWorkflowMochi(len,width,height,fps,crf,cfg_exc + mochi, prompt))
    sendWorkflow(setWorkflowWan3(len,width,height,fps,crf,cfg_exc + wan3, prompt))
    sendWorkflow(setWorkflowWan14(len,width,height,fps,crf, cfg_exc + wan14,prompt))


    width = 640
    height = 480
    len = 50
    fps = 5
    crf = 32
    cfg_exc = -1



    sendWorkflow(setWorkflowLTXIMAGEM(len,width,height,fps,crf,cfg_exc + ltximg, prompt))
    sendWorkflow(setWorkflowLX(len,width,height,fps,crf,cfg_exc + ltxText, prompt))
    sendWorkflow(setWorkflowMochi(len,width,height,fps,crf,cfg_exc + mochi, prompt))
    sendWorkflow(setWorkflowWan3(len,width,height,fps,crf,cfg_exc + wan3, prompt))
    sendWorkflow(setWorkflowWan14(len,width,height,fps,crf, cfg_exc + wan14,prompt))






    prompt = ". In cartoon Disney style and 9:16 aspect ratio. A little girl are faced with many shiny toys and colorful sweets, a little girl takes a coin in her hands, but then sees a magical piggy bank in the shape of a star."

    width = 320
    height = 240
    len = 50
    fps = 5
    crf = 32
    cfg_exc = 0



    sendWorkflow(setWorkflowLTXIMAGEM(len,width,height,fps,crf,cfg_exc + ltximg, prompt))
    sendWorkflow(setWorkflowLX(len,width,height,fps,crf,cfg_exc + ltxText, prompt))
    sendWorkflow(setWorkflowMochi(len,width,height,fps,crf,cfg_exc + mochi, prompt))
    sendWorkflow(setWorkflowWan3(len,width,height,fps,crf,cfg_exc + wan3, prompt))
    sendWorkflow(setWorkflowWan14(len,width,height,fps,crf, cfg_exc + wan14,prompt))

    width = 320
    height = 240
    len = 50
    fps = 5
    crf = 32
    cfg_exc = 0.5


    sendWorkflow(setWorkflowLTXIMAGEM(len,width,height,fps,crf,cfg_exc + ltximg, prompt))
    sendWorkflow(setWorkflowLX(len,width,height,fps,crf,cfg_exc + ltxText, prompt))
    sendWorkflow(setWorkflowMochi(len,width,height,fps,crf,cfg_exc + mochi, prompt))
    sendWorkflow(setWorkflowWan3(len,width,height,fps,crf,cfg_exc + wan3, prompt))
    sendWorkflow(setWorkflowWan14(len,width,height,fps,crf, cfg_exc + wan14,prompt))


    width = 320
    height = 240
    len = 50
    fps = 5
    crf = 32
    cfg_exc = 1


    sendWorkflow(setWorkflowLTXIMAGEM(len,width,height,fps,crf,cfg_exc + ltximg, prompt))
    sendWorkflow(setWorkflowLX(len,width,height,fps,crf,cfg_exc + ltxText, prompt))
    sendWorkflow(setWorkflowMochi(len,width,height,fps,crf,cfg_exc + mochi, prompt))
    sendWorkflow(setWorkflowWan3(len,width,height,fps,crf,cfg_exc + wan3, prompt))
    sendWorkflow(setWorkflowWan14(len,width,height,fps,crf, cfg_exc + wan14,prompt))


    width = 320
    height = 240
    len = 50
    fps = 5
    crf = 32
    cfg_exc = -0.5



    sendWorkflow(setWorkflowLTXIMAGEM(len,width,height,fps,crf,cfg_exc + ltximg, prompt))
    sendWorkflow(setWorkflowLX(len,width,height,fps,crf,cfg_exc + ltxText, prompt))
    sendWorkflow(setWorkflowMochi(len,width,height,fps,crf,cfg_exc + mochi, prompt))
    sendWorkflow(setWorkflowWan3(len,width,height,fps,crf,cfg_exc + wan3, prompt))
    sendWorkflow(setWorkflowWan14(len,width,height,fps,crf, cfg_exc + wan14,prompt))


    width = 320
    height = 240
    len = 50
    fps = 5
    crf = 32
    cfg_exc = -1



    sendWorkflow(setWorkflowLTXIMAGEM(len,width,height,fps,crf,cfg_exc + ltximg, prompt))
    sendWorkflow(setWorkflowLX(len,width,height,fps,crf,cfg_exc + ltxText, prompt))
    sendWorkflow(setWorkflowMochi(len,width,height,fps,crf,cfg_exc + mochi, prompt))
    sendWorkflow(setWorkflowWan3(len,width,height,fps,crf,cfg_exc + wan3, prompt))
    sendWorkflow(setWorkflowWan14(len,width,height,fps,crf, cfg_exc + wan14,prompt))












    ##########################

    width = 320
    height = 240
    len = 96
    fps = 5
    crf = 32
    cfg_exc = 0.5


    sendWorkflow(setWorkflowLTXIMAGEM(len,width,height,fps,crf,cfg_exc + ltximg, prompt))
    sendWorkflow(setWorkflowLX(len,width,height,fps,crf,cfg_exc + ltxText, prompt))
    sendWorkflow(setWorkflowMochi(len,width,height,fps,crf,cfg_exc + mochi, prompt))
    sendWorkflow(setWorkflowWan3(len,width,height,fps,crf,cfg_exc + wan3, prompt))
    sendWorkflow(setWorkflowWan14(len,width,height,fps,crf, cfg_exc + wan14,prompt))


    width = 320
    height = 240
    len = 96
    fps = 5
    crf = 32
    cfg_exc = 1


    sendWorkflow(setWorkflowLTXIMAGEM(len,width,height,fps,crf,cfg_exc + ltximg, prompt))
    sendWorkflow(setWorkflowLX(len,width,height,fps,crf,cfg_exc + ltxText, prompt))
    sendWorkflow(setWorkflowMochi(len,width,height,fps,crf,cfg_exc + mochi, prompt))
    sendWorkflow(setWorkflowWan3(len,width,height,fps,crf,cfg_exc + wan3, prompt))
    sendWorkflow(setWorkflowWan14(len,width,height,fps,crf, cfg_exc + wan14,prompt))


    width = 320
    height = 240
    len = 96
    fps = 5
    crf = 32
    cfg_exc = -0.5



    sendWorkflow(setWorkflowLTXIMAGEM(len,width,height,fps,crf,cfg_exc + ltximg, prompt))
    sendWorkflow(setWorkflowLX(len,width,height,fps,crf,cfg_exc + ltxText, prompt))
    sendWorkflow(setWorkflowMochi(len,width,height,fps,crf,cfg_exc + mochi, prompt))
    sendWorkflow(setWorkflowWan3(len,width,height,fps,crf,cfg_exc + wan3, prompt))
    sendWorkflow(setWorkflowWan14(len,width,height,fps,crf, cfg_exc + wan14,prompt))


    width = 320
    height = 240
    len = 96
    fps = 5
    crf = 32
    cfg_exc = -1



    sendWorkflow(setWorkflowLTXIMAGEM(len,width,height,fps,crf,cfg_exc + ltximg, prompt))
    sendWorkflow(setWorkflowLX(len,width,height,fps,crf,cfg_exc + ltxText, prompt))
    sendWorkflow(setWorkflowMochi(len,width,height,fps,crf,cfg_exc + mochi, prompt))
    sendWorkflow(setWorkflowWan3(len,width,height,fps,crf,cfg_exc + wan3, prompt))
    sendWorkflow(setWorkflowWan14(len,width,height,fps,crf, cfg_exc + wan14,prompt))

    width = 640
    height = 480
    len = 50
    fps = 5
    crf = 32
    cfg_exc = 0.5


    sendWorkflow(setWorkflowLTXIMAGEM(len,width,height,fps,crf,cfg_exc + ltximg, prompt))
    sendWorkflow(setWorkflowLX(len,width,height,fps,crf,cfg_exc + ltxText, prompt))
    sendWorkflow(setWorkflowMochi(len,width,height,fps,crf,cfg_exc + mochi, prompt))
    sendWorkflow(setWorkflowWan3(len,width,height,fps,crf,cfg_exc + wan3, prompt))
    sendWorkflow(setWorkflowWan14(len,width,height,fps,crf, cfg_exc + wan14,prompt))


    width = 640
    height = 480
    len = 50
    fps = 5
    crf = 32
    cfg_exc = 1


    sendWorkflow(setWorkflowLTXIMAGEM(len,width,height,fps,crf,cfg_exc + ltximg, prompt))
    sendWorkflow(setWorkflowLX(len,width,height,fps,crf,cfg_exc + ltxText, prompt))
    sendWorkflow(setWorkflowMochi(len,width,height,fps,crf,cfg_exc + mochi, prompt))
    sendWorkflow(setWorkflowWan3(len,width,height,fps,crf,cfg_exc + wan3, prompt))
    sendWorkflow(setWorkflowWan14(len,width,height,fps,crf, cfg_exc + wan14,prompt))


    width = 640
    height = 480
    len = 50
    fps = 5
    crf = 32
    cfg_exc = -0.5



    sendWorkflow(setWorkflowLTXIMAGEM(len,width,height,fps,crf,cfg_exc + ltximg, prompt))
    sendWorkflow(setWorkflowLX(len,width,height,fps,crf,cfg_exc + ltxText, prompt))
    sendWorkflow(setWorkflowMochi(len,width,height,fps,crf,cfg_exc + mochi, prompt))
    sendWorkflow(setWorkflowWan3(len,width,height,fps,crf,cfg_exc + wan3, prompt))
    sendWorkflow(setWorkflowWan14(len,width,height,fps,crf, cfg_exc + wan14,prompt))


    width = 640
    height = 480
    len = 50
    fps = 5
    crf = 32
    cfg_exc = -1



    sendWorkflow(setWorkflowLTXIMAGEM(len,width,height,fps,crf,cfg_exc + ltximg, prompt))
    sendWorkflow(setWorkflowLX(len,width,height,fps,crf,cfg_exc + ltxText, prompt))
    sendWorkflow(setWorkflowMochi(len,width,height,fps,crf,cfg_exc + mochi, prompt))
    sendWorkflow(setWorkflowWan3(len,width,height,fps,crf,cfg_exc + wan3, prompt))
    sendWorkflow(setWorkflowWan14(len,width,height,fps,crf, cfg_exc + wan14,prompt))

def send(id, scenes):

    num = 0
    for i in scenes:
        num = num + 1
        prompt = setWorkflowFinish(i, num, id)
        sendWorkflow(prompt)


if __name__ == "__main__":
    scenes = [
        "A little girl with curly hair and a blue dress walks smiling through the busy streets of the city, holding a small white kitten with bright eyes in her arms. The store windows shine with colorful lights and several people pass by in a hurry."
        
        , "The little girl with curly hair and a blue dress stops in front of a store full of colorful toys. Her eyes shine as she sees a beautiful doll in a pink dress displayed in the window. The small white kitten, in her arms, blinks curiously.",
        
        "The little girl with curly hair and a blue dress squeezes the white kitten in her arms and looks anxiously at the window, wishing to take the doll home. The store lights reflect on her excited face.",
        
        "The little girl with curly hair and a blue dress opens her small pink purse and finds only a few coins. Her face falls as she realizes she doesn't have enough money to buy the doll. The white kitten watches her with attentive eyes.",
        
        "The small white kitten, with bright eyes, raises its ears and tilts its head, observing the thoughtful expression of the little girl with curly hair and a blue dress. The little girl sighs and strokes her feline friend.",
        
        "The little girl with curly hair and a blue dress decides that she will save up to buy the doll. She smiles determinedly and hugs her small white kitten, who meows softly in response.",
        
        "In the room decorated with stars on the wall, the little girl with curly hair and a blue dress holds a pink piggy bank shaped like a pig. The small white kitten is beside her, watching curiously.",
        
        "Every day, the little girl with curly hair and a blue dress puts a golden coin in the piggy bank. The small white kitten sits beside her, wagging its tail while watching.",
        
        "The little girl with curly hair and a blue dress smiles as she sees the piggy bank getting heavier. The small white kitten lightly touches the bank with its paw, curious about the sound of the coins.",
        
        "After many days of saving, the pink piggy bank is full. The little girl with curly hair and a blue dress smiles proudly. The small white kitten meows happily beside her.",
        
        "The little girl with curly hair and a blue dress walks excitedly through the city again, holding the small white kitten in her arms. They arrive in front of the toy store.",
        
        "With her hands full of coins, the little girl with curly hair and a blue dress buys the doll she wanted so much. Her eyes shine with happiness. The small white kitten is beside her, purring with joy.",
        
        "Sitting in her room decorated with stars, the little girl with curly hair and a blue dress hugs the new doll. The small white kitten curls up beside her, satisfied.",
        
        "The small white kitten with bright eyes touches the doll with its paw and purrs happily. The little girl with curly hair and a blue dress laughs and hugs her feline friend.",
        
        "The little girl with curly hair and a blue dress decides that she will always save money before buying something special. The small white kitten meows softly, as if agreeing."
    ]
    send(2, scenes)
    # teste()

    print("Cena Finalizada!")



