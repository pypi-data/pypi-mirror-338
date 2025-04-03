export interface GPUConfig {
  type: 'H200' | 'A100' | 'L4';
  memoryGB: number;
}

export const GPU_CONFIGS: Record<GPUConfig['type'], GPUConfig> = {
  H200: {
    type: 'H200',
    memoryGB: 141
  },
  A100: {
    type: 'A100',
    memoryGB: 40
  },
  L4: {
    type: 'L4',
    memoryGB: 24
  }
};

export const DEFAULT_GPU_CONFIG = GPU_CONFIGS.A100; 