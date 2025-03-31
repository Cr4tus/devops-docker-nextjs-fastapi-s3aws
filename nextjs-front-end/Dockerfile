ARG NODE=node:23-alpine

# Stage 1: Install the dependencies
FROM ${NODE} as dependencies

RUN apk add --no-cache libc6-compat
WORKDIR /app

COPY ./package.json ./yarn.lock* ./
RUN yarn --frozen-lockfile

# Stage 2: Build the app
FROM ${NODE} AS app-builder

WORKDIR /app
COPY --from=dependencies /app/node_modules ./node_modules
COPY . .

RUN yarn build

# Stage 3: Run the production build
FROM ${NODE} AS app-runner-production

WORKDIR /app

ENV NODE_ENV production

COPY --from=app-builder /app/public ./public
COPY --from=app-builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=app-builder --chown=nextjs:nodejs /app/.next/static ./.next/static

RUN addgroup --system --gid 1001 nodejs
RUN adduser  --system --uid 1001 nextjs

USER nextjs

EXPOSE 3000
ENV PORT 3000
ENV HOSTNAME 0.0.0.0
CMD ["node", "server.js"]